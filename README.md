# The Semigroups package - Zero to ε

This repository contains the source code for the workshop "The Semigroups package - Zero to ε" at the
[NBSAN](https://manchester-semigroups.github.io/NBSAN/index.html) meeting on the 19th of May 2026 in Manchester.

## Prerequisites

The online worksheets are made using the [`mkdocs`](https://www.mkdocs.org/) tool with the
[`mkdocs-material`](https://squidfunk.github.io/mkdocs-material/) theme.
Install them using:

```bash
python3 -m pip install mkdocs mkdocs-material
```

The webpage can then be compiled and served by running the following command in the root directory of the repository
```bash
mkdocs serve
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
