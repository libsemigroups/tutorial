# The Semigroups package - Zero to ε

This repository contains the source code for the workshop "The Semigroups package - Zero to ε" at the
[NBSAN](https://manchester-semigroups.github.io/NBSAN/index.html) meeting on the 19th of May 2026 in Manchester.

## Prerequisites

The online worksheets are made using the [`mkdocs`](https://www.mkdocs.org/) tool with the
[`mkdocs-material`](https://squidfunk.github.io/mkdocs-material/) theme.
Install them using:

```bash
python3 -m pip install mkdocs mkdocs-material mkdocs-awesome-nav
```

The webpage can then be compiled and served by running the following command in the root directory of the repository
```bash
mkdocs serve
```

The site header displays the tutorial release tag when built by the release
workflow, with a link to that release on GitHub. Local builds display `dev`.
To preview a release badge locally, set `TUTORIAL_VERSION` and
`TUTORIAL_RELEASE_TAG`, for example:

```bash
TUTORIAL_VERSION=v0.2.0 TUTORIAL_RELEASE_TAG=v0.2.0 mkdocs serve
```

The Changelog page is populated from the published releases of
[`libsemigroups/tutorial`](https://github.com/libsemigroups/tutorial/releases)
each time the site builds. Edit release descriptions on GitHub; no local copy of
the release notes needs to be maintained. Publishing a release rebuilds and
deploys the site automatically. To refresh the site after editing an existing
release description, run the Documentation workflow manually.

Building the changelog requires access to the GitHub API. Local builds work
without authentication, but you can set `GITHUB_TOKEN` to avoid the lower
unauthenticated rate limit. The build fails if release notes cannot be fetched,
so an incomplete changelog is never deployed. Both workflows provide their
built-in GitHub token automatically.

To run the changelog tests locally:

```bash
python3 -m unittest discover -s tests
```

## Adding content

To add content to the worksheet, simply add a new markdown file in any subfolder of the `docs/` directory and
link it in the navigation bar by modifying the `nav` section of the `mkdocs.yml` file, e.g. the initial
`mkdocs.yml` file could look something like

```yml
nav:
  - Home: index.md
  - Semigroups:
    - gap/index.md
    - Installation: gap/install.md
    - 'The GAP Session': gap/session.md
    - 'Worksheet 1: Analysis of finite semigroups': gap/worksheet1.md
```

to add a new section `libsemigroups_pybind11` consisting of two files, an index
`libsemigroups_pybind11/index.md` and install instructions `libsemigroups_pybind11/install.md`, we would modify the
`nav` section to look like

```yml
nav:
  - Home: index.md
  - Semigroups:
    - gap/index.md
    - Installation: gap/install.md
    - 'The GAP Session': gap/session.md
    - 'Worksheet 1: Analysis of finite semigroups': gap/worksheet1.md
  - libsemigroups_pybind11:
    - libsemigroups_pybind11/index.md
    - Installation: libsemigroups_pybind11/install.md
```

Note: the first unlabelled element of a subsection will be used as the subsection index, i.e. it won't appear as a
separate entry in the navigation bar. So here the `libsemigroups_pybind11/index.md` file will simply be used
for the `libsemigroups_pybind11` section, and
`libsemigroups_pybind11/install.md` will be used as the contents for the `Installation` subsection.
