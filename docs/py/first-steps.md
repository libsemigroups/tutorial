# First steps --- libsemigroups_pybind11

Now that you've successfully installed `libsemigroups_pybind11`, this page
explains a few ways to start using it; see [Installation](install.md).

If you are familiar with [Jupyter](https://jupyter.org/) notebooks and/or are
comfortable with using the Python interpreter, then you can skim this page and
continue with the examples in the rest of the tutorial.

This guide assumes you are familiar with programming in [Python](https://www.python.org), if you are not, then take a look at [Software Carpentry Programming With Python](https://swcarpentry.github.io/python-novice-inflammation/)

## Using [IPython](https://ipython.org/) in a terminal

The terminal is an application where you can type commands. The name of the
terminal application depends on your operating system:

- on macOS, open **Terminal**;
- on Linux, open the terminal application provided by your desktop environment.

If you installed `libsemigroups_pybind11` in a conda or mamba environment, first
activate that environment:

```console
$ mamba activate libsemigroups_pybind11
```

If you chose a different environment name during installation, use that name
instead.

Next start [IPython](https://ipython.org/):

```console
$ ipython
```

You should now see a prompt beginning with `In [1]:`. Import
`libsemigroups_pybind11` as follows:

```python
import libsemigroups_pybind11
```

You can also import the particular classes and functions you want to use:

```python
from libsemigroups_pybind11 import FroidurePin, Transf
```

For example:

```python
f = Transf([1, 0])
g = Transf([0, 0])
S = FroidurePin([f, g])
S.size()
```

To leave IPython, type:

```python
exit
```

or press `Ctrl-D`.

## Using a local [Jupyter](https://jupyter.org/) notebook

A [Jupyter](https://jupyter.org/) notebook is often more convenient than a
terminal session because you can keep code, output, notes, and plots together in
one place.

If you installed `libsemigroups_pybind11` in a conda or mamba environment,
activate it first:

```console
$ mamba activate libsemigroups_pybind11
```

Then start [Jupyter](https://jupyter.org/):

```console
$ jupyter notebook
```

This should open [Jupyter](https://jupyter.org/) in your web browser. Create a
new notebook and type the following into the first code cell:

```python
import libsemigroups_pybind11
```

Run the cell. If it finishes without an error, then the notebook can see your
installation of `libsemigroups_pybind11`.

You can use the same imports as in [IPython](https://ipython.org/):

```python
from libsemigroups_pybind11 import FroidurePin, Transf

S = FroidurePin([Transf([1, 0]), Transf([0, 0])])
S.size()
```

When you have finished, choose **File > Save and Checkpoint** in
[Jupyter](https://jupyter.org/), then stop the notebook server from the terminal
by pressing `Ctrl-C`.

## Using an online notebook service

You can also use a notebook service that runs Python in a web browser. This is
useful if you cannot install software on your own computer, or if you want to
share a notebook with someone else. Examples include
[Google Colab](https://colab.research.google.com/),
[Binder](https://mybinder.org/), [CoCalc](https://cocalc.com/), and hosted
[JupyterLab](https://jupyter.org/) services.

The details differ from service to service, but the general idea is:

1. Create a new Python notebook.
2. Install `libsemigroups_pybind11` in the notebook.
3. Import `libsemigroups_pybind11` in a later cell.

For services that allow `pip` installs from a notebook cell, the first cell can
usually be:

```python
%pip install libsemigroups_pybind11
```

After that cell has finished, run:

```python
import libsemigroups_pybind11
```

or:

```python
from libsemigroups_pybind11 import FroidurePin, Transf
```

Some services reset the Python environment when the notebook is closed. If that
happens, run the installation cell again the next time you open the notebook.

Hosted notebook services may use different Python versions or operating systems
from your own computer. If `pip install libsemigroups_pybind11` fails on one
service, try running the notebook locally, or use a service that supports
conda/mamba environments.

## Checking that the import worked

In [IPython](https://ipython.org/), a local notebook, or an online notebook, a
successful import usually prints nothing. To check that Python has found the
package, you can run:

```python
import libsemigroups_pybind11
dir(libsemigroups_pybind11)
```

This should print a list of names provided by `libsemigroups_pybind11`.
