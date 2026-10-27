"""Checks for GitHub pagination, release rendering, and build failures."""

import io
import json
import os
import unittest
from types import SimpleNamespace
from unittest.mock import patch
from urllib.error import HTTPError, URLError

import markdown
from mkdocs.exceptions import PluginError

from hooks import changelog


def release(tag="v1.0.0", **changes):
    result = {
        "tag_name": tag,
        "html_url": f"https://github.com/libsemigroups/tutorial/releases/tag/{tag}",
        "published_at": "2026-10-27T09:32:06Z",
        "draft": False,
        "prerelease": False,
        "body": "Fix some typos.",
    }
    result.update(changes)
    return result


def response(releases):
    return io.BytesIO(json.dumps(releases).encode())


class FetchReleasesTests(unittest.TestCase):
    @patch.dict(os.environ, {"GITHUB_TOKEN": "test-token"})
    @patch.object(changelog, "urlopen")
    def test_fetches_all_pages_filters_drafts_and_sorts_by_publication(self, urlopen):
        older = release("v0.9.0", published_at="2026-01-01T00:00:00Z")
        newer = release("v1.1.0")
        urlopen.side_effect = [
            response([older] * 99 + [release("v2.0.0", draft=True)]),
            response([newer]),
        ]

        releases = changelog.fetch_releases()

        self.assertEqual(len(releases), 100)
        self.assertEqual(releases[0], newer)
        self.assertTrue(all(not item["draft"] for item in releases))
        requests = [call.args[0] for call in urlopen.call_args_list]
        self.assertEqual(requests[0].full_url, changelog.RELEASES_API + "?per_page=100&page=1")
        self.assertEqual(requests[1].full_url, changelog.RELEASES_API + "?per_page=100&page=2")
        self.assertEqual(requests[0].get_header("Authorization"), "Bearer test-token")
        self.assertEqual(urlopen.call_args.kwargs["timeout"], 30)

    @patch.dict(os.environ, {"GITHUB_TOKEN": ""})
    @patch.object(changelog, "urlopen", return_value=response([]))
    def test_public_builds_need_no_token(self, urlopen):
        self.assertEqual(changelog.fetch_releases(), [])
        self.assertIsNone(urlopen.call_args.args[0].get_header("Authorization"))


class ChangelogPageTests(unittest.TestCase):
    def setUp(self):
        self.page = SimpleNamespace(file=SimpleNamespace(src_uri="changelog.md"))

    @patch.object(changelog, "fetch_releases")
    def test_other_pages_do_not_fetch_releases(self, fetch):
        page = SimpleNamespace(file=SimpleNamespace(src_uri="index.md"))
        self.assertEqual(changelog.on_page_markdown("# Home", page), "# Home")
        fetch.assert_not_called()

    @patch.object(changelog, "fetch_releases")
    def test_notes_render_as_markdown_under_each_release(self, fetch):
        fetch.return_value = [
            release(body="## What's Changed\r\n\r\n* Fix **typos**.\r\n\r\n```python\r\n# Keep this comment\r\n```"),
            release("v0.9.0", body=None, prerelease=True),
        ]

        result = changelog.on_page_markdown("# Changelog\n", self.page)
        html = markdown.markdown(result, extensions=["fenced_code", "toc"])

        self.assertIn('<h2 id="v100">v1.0.0</h2>', html)
        self.assertIn('<h3 id="whats-changed">What\'s Changed</h3>', html)
        self.assertIn("<li>Fix <strong>typos</strong>.</li>", html)
        self.assertIn("# Keep this comment", html)
        self.assertNotIn("### Keep this comment", html)
        self.assertIn("2026-10-27 · Pre-release", html)
        self.assertIn("No release description provided.", html)
        self.assertIn('href="https://github.com/libsemigroups/tutorial/releases/tag/v1.0.0"', html)

    @patch.object(changelog, "fetch_releases", return_value=[])
    def test_no_releases_has_an_explicit_empty_state(self, fetch):
        result = changelog.on_page_markdown("# Changelog\n", self.page)
        self.assertIn("No releases have been published yet.", result)

    def test_tilde_fences_and_long_backtick_fences_are_preserved(self):
        body = "# Notes\n\n~~~~\n## Code comment\n~~~~\n\n````markdown\n```\n# Example\n```\n````\n\n## Fixes"
        expected = body.replace("# Notes", "### Notes").replace("## Fixes", "### Fixes")
        self.assertEqual(changelog.nest_headings(body), expected)

    def test_api_errors_abort_the_build(self):
        errors = [
            URLError("Network unavailable"),
            HTTPError(changelog.RELEASES_API, 403, "Rate limit exceeded", {}, None),
            ValueError("Invalid JSON"),
        ]
        for error in errors:
            with self.subTest(error=error):
                with patch.object(changelog, "fetch_releases", side_effect=error):
                    with self.assertRaisesRegex(PluginError, "Could not load.*GitHub"):
                        changelog.on_page_markdown("# Changelog\n", self.page)


if __name__ == "__main__":
    unittest.main()
