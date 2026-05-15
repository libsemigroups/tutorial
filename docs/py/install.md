# Installation in Python

`libsemigroups_pybind11` is compatible with Python versions TODO

## Installing with pip

It's possible to install `libsemigroups_pybind11` using `pip` by doing
one of the following (depending on your system and setup):

```console
$ pip install libsemigroups_pybind11
```

```console
$ pip3 install libsemigroups_pybind11
```

```console
$ python -m pip install libsemigroups_pybind11
```

## Installing with mamba

This installation method assumes that you have anaconda or miniconda
installed. See the [getting started](http://bit.ly/33B0Vfs) and
[miniconda download page](https://conda.io/miniconda.html) on the
[conda](https://conda.io/) website.

It might be a good idea to create and activate a conda/mamba environment
to contain the installation of the `libsemigroups_pybind11`:

```console
$ mamba create --name myenv_name libsemigroups_pybind11
$ mamba activate myenv_name
```

Here's the contents of sample `environment.yml` file that you can use to create
a mamba environment that contains everything you might need to complete this
tutorial.

Create a file named `environment.yml` and copy/paste the following into that
file:

```yml
channels:
  - conda-forge
dependencies:
  - graphviz
  - ipython
  - jupyter
  - libsemigroups_pybind11
```

Save the file and then in the terminal:

```bash
mamba env create -f environment.yml --name libsemigroups_pybind11
```

Every time you want to use `libsemigroups_pybind11` make sure type the
following into the terminal:

```bash
mamba activate libsemigroups_pybind11
```

## Adding libsemigroups as a dependency to your project using uv

If you manage a Python project with [uv](https://docs.astral.sh/uv), you
can add libsemigroups as a dependency as follows:

```console
$ uv add libsemigroups_pybind11
```

For more information, see uv's guide on [managing
dependencies](https://docs.astral.sh/uv/concepts/projects/dependencies/).
