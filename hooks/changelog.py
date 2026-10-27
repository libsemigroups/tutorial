"""Populate the changelog with GitHub release descriptions at build time."""

import json
import os
import re
from urllib.error import URLError
from urllib.request import Request, urlopen

from mkdocs.exceptions import PluginError


RELEASES_API = "https://api.github.com/repos/libsemigroups/tutorial/releases"


def fetch_releases():
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "libsemigroups-tutorial-changelog",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if token:
        headers["Authorization"] = f"Bearer {token}"

    releases = []
    page = 1
    while True:
        request = Request(f"{RELEASES_API}?per_page=100&page={page}", headers=headers)
        with urlopen(request, timeout=30) as response:
            batch = json.load(response)
        releases.extend(release for release in batch if not release["draft"])
        if len(batch) < 100:
            break
        page += 1

    return sorted(releases, key=lambda release: release["published_at"], reverse=True)


def nest_headings(body):
    """Keep note headings below release headings, preserving fenced code."""
    lines = []
    fence = None
    for line in body.splitlines():
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence:
            if (
                marker
                and marker[1][0] == fence[0]
                and len(marker[1]) >= len(fence)
                and not marker[2].strip()
            ):
                fence = None
        elif marker:
            fence = marker[1]
        else:
            heading = re.match(r"^( {0,3})(#{1,6})(\s+|$)(.*)$", line)
            if heading:
                depth = min(6, max(3, len(heading[2]) + 1))
                line = heading[1] + "#" * depth + heading[3] + heading[4]
        lines.append(line)
    return "\n".join(lines)


def render_releases(releases):
    if not releases:
        return "No releases have been published yet.\n"

    sections = []
    for release in releases:
        tag = release["tag_name"]
        date = release["published_at"][:10]
        status = " · Pre-release" if release["prerelease"] else ""
        body = (release.get("body") or "").strip()
        sections.append(
            f"## {tag}\n\n"
            f"{date}{status} · [View on GitHub]({release['html_url']})\n\n"
            f"{nest_headings(body) if body else 'No release description provided.'}"
        )
    return "\n\n".join(sections) + "\n"


def on_page_markdown(markdown, page, **kwargs):
    if page.file.src_uri != "changelog.md":
        return markdown

    try:
        releases = fetch_releases()
    except (URLError, OSError, ValueError, KeyError, TypeError) as error:
        raise PluginError(
            "Could not load the tutorial changelog from GitHub. "
            "Check the network connection and, if set, GITHUB_TOKEN. "
            f"GitHub error: {error}"
        ) from error
    return markdown + "\n" + render_releases(releases)
