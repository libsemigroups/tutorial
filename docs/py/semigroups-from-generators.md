# Semigroups and monoids defined by generators

On [the previous page](fp.md), you saw how to construct and compute with
semigroups and monoids defined from presentations. On this page, you will learn
about presentations defined by a collection of generators. In particular, you
will learn which type of objects can be used as generators of a semigroup, and
how to compute with semigroups defined by generators.

## Elements

In `libsemigroups_pybind11`, there are several types of object that can be
treated as elements of a semigroup, which are broken down into four categories:

1. Bipartitions,
1. Matrices,
1. Partitioned binary relations (PBRs), and
1. Transformations.

In this this section, you will learn how to construct objects of these types in
`libsemigroups_pybind11`.

!!! note

    This section provides examples of how to use different types of semigroup
    element, but does not attempt to showcase every feature or function. For a
    full description of the API for the different element types, see the
    [Elements](https://libsemigroups.github.io/libsemigroups_pybind11/data-structures/elements/index.html)
    page in the `libsemigroups_pybind11` documentation.

### Bipartitions

Let $n\in \mathbb{N}$, and define $\mathbf{n} =\{1, 2,\dots, n\}$, and
$-\mathbf{n} =\{-1, -2,\dots, -n\}$. A _bipartition of degree \(n\)_ is a
partition of $\mathbf{n} \cup -\mathbf{n}$. The constituent subsets of a
bipartition are called _blocks_. Semigroups (namely _partition semigroups_) can
be defined over bipartitions using the following multiplication.

Let $x$ and $y$ be bipartitions of degree $n$. Define
$\mathbf{n}' = \{1', 2', \dots, n'\}$. From $x$, create a partition $x'$ of the
set $\mathbf{n} \cup \mathbf{n}'$ by replacing each negative point $-i$ in a
block of $x$ by the point $i'$, and create from y a partition $y'$ of the set
$\mathbf{n}' \cup -\mathbf{n}$ by replacing each positive point $i$ in a block
of $y$ by the point $i'$. Then define a relation on the set
$\mathbf{n} \cup \mathbf{n}'\cup -\mathbf{n}$, where $i$ and $j$ are related if
they are related in either $x'$ or $y'$, and let $p$ be the transitive closure
of this relation. Finally, define $xy$ to be the bipartition of degree $n$ given
by the restriction of the equivalence relation $p$ to the set
$\mathbf{n} \cup -\mathbf{n}$.

Constructing bipartitions in `libsemigroups_pybind` can be done by specifying
their blocks:

```python
from libsemigroups_pybind11 import Bipartition
x = Bipartition([[1, -1, -2], [2, 5], [3, 4, -3], [-4, -5]])
y = Bipartition([[1, -4], [2], [3, -1], [4], [5, -3], [-2], [-5]])
```

This defines the bipartitions that correspond to

![bipartition x](/images/bipartition_1.svg)

and

![bipartition y](/images/bipartition_2.svg).

You can multiply these bipartitions together using the `*` operator:

```python
x*y # returns Bipartition([[1, -4], [2, 5], [3, 4, -1], [-2], [-3], [-5]])
```

If you want to construct a random bipartition of some fixed degree, you can use
the `bipartition.random` function:

```python
from libsemigroups_pybind11 import bipartition
bipartition.random(7)
```

### Matrices

There are several different flavours of matrix available in
`libsemigroups_pybind11`. For example, you can construct the $3 \times 3$ matrix

$$
    m =
    \begin{bmatrix}
        0 & 1 & 0 \\
        0 & 1 & 1 \\
        1 & 1 & 1
    \end{bmatrix}
$$

over the integers in the following way:

```python
from libsemigroups_pybind11 import Matrix, MatrixKind
m = Matrix(MatrixKind.Integer, [[0, 1, 0], [0, 1, 1], [1, 1, 1]])
```

These matrices can be added, multiplied, and exponentiated using the the `+`,
`*` and `**` operators:

```python
m + m
# returns
# Matrix(MatrixKind.Integer, [[0, 2, 0],
#                             [0, 2, 2],
#                             [2, 2, 2]])

m * m
# returns
# Matrix(MatrixKind.Integer, [[0, 1, 1],
#                             [1, 2, 2],
#                             [1, 3, 2]])

m ** 3
# returns
# Matrix(MatrixKind.Integer, [[1, 2, 2],
#                             [2, 5, 4],
#                             [2, 6, 5]])
```

In general, `Matrix` objects in `libsemigroups_pybind11` are constructed by
specifying a value from the `MatrixKind` enum, and a list of rows of values.
The `MatrixKind` value determines what type of matrix is returned, and the
possible values are summarised in the following table.

| Value          | Description                                                              |
| :------------- | :----------------------------------------------------------------------- |
| `Boolean`      | Boolean matrices                                                         |
| `Integer`      | Integer matrices                                                         |
| `MaxPlus`      | Matrices over the tropical max-plus semiring                             |
| `MinPlus`      | Matrices over the tropical min-plus semiring                             |
| `ProjMaxPlus`  | Projective matrices over the tropical max-plus semiring                  |
| `ProjMinPlus`  | Projective matrices over the tropical min-plus semiring                  |
| `MaxPlusTrunc` | Matrices over the truncated tropical max-plus semiring                   |
| `MinPlusTrunc` | Matrices over the truncated tropical min-plus semiring                   |
| `NTP`          | Matrices over the semiring of natural numbers quotiented by $t = t + p$. |

Therefore, if we instead want to interpret $m$ as a boolean matrix, this can be achieved in the
following way

```python
from libsemigroups_pybind11 import Matrix, MatrixKind
m = Matrix(MatrixKind.Boolean, [[0, 1, 0], [0, 1, 1], [1, 1, 1]])
m + m
# returns
# Matrix(MatrixKind.Boolean, [[0, 1, 0],
#                             [0, 1, 1],
#                             [1, 1, 1]])

m * m
# returns
# Matrix(MatrixKind.Boolean, [[0, 1, 1],
#                             [1, 1, 1],
#                             [1, 1, 1]])

m ** 3
# returns
# Matrix(MatrixKind.Boolean, [[1, 1, 1],
#                             [1, 1, 1],
#                             [1, 1, 1]])
```

!!! note

    When representing boolean matrices of dimension up to $8 \times 8$, you can
    use the class `BMat8` to take advantage of some compiler optimisations. More
    information can be found on the [BMat8 class](https://libsemigroups.github.io/libsemigroups_pybind11/data-structures/elements/matrix/bmat8.html) page in the `libsemigroups_pybind11` documentation.

### Transformations

### Partitioned binary relations (PBRs)

## Finitely generated semigroups

### `FroidurePin`

### `Konieczny`

### `SchreierSims`
