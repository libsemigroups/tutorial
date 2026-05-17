# Semigroups and monoids defined by generators

If you followed the instructions on [the previous page](first-steps.md), you
should now have a functioning version of `libsemigroups_pybind11`. On this page,
you will learn about semigroups defined by a collection of generators. In
particular, you will learn which type of objects can be used as generators of a
semigroup, and how to compute with semigroups defined by generators.

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

    This section provides examples of how to create different types of semigroup
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

<figure markdown="span">
	![bipartition x](/images/bipartition_1.svg)
</figure>
and
<figure markdown="span">
	![bipartition y](/images/bipartition_2.svg)
</figure>

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

!!! info

    For more information about bipartitions, see the [Bipartition class](https://libsemigroups.github.io/libsemigroups_pybind11/data-structures/elements/bipart/bipart.html) and
    [Bipartition helpers](https://libsemigroups.github.io/libsemigroups_pybind11/data-structures/elements/bipart/bipart-helpers.html)
    pages in the `libsemigroups_pybind11` documentation.

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

Therefore, if you instead want to interpret $m$ as a boolean matrix, this can be achieved in the
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

!!! info

    For more information about matrices, see the [Matrix class](https://libsemigroups.github.io/libsemigroups_pybind11/data-structures/elements/matrix/matrix.html) and
    [Matrix helpers](https://libsemigroups.github.io/libsemigroups_pybind11/data-structures/elements/matrix/matrix-helpers.html)
    pages in the `libsemigroups_pybind11` documentation.

### Transformations

### Partitioned binary relations (PBRs)

## Finitely generated semigroups

In this section, now that you have seen which types of objects can be treated as
semigroup elements, you will learn how to compute with semigroups constructed
from a collection of generators. The focus will be on the algorithms and
functions implemented in the classes `FroidurePin` and `Konieczny`.

### `FroidurePin`

[^1]:
    Froidure, Véronique & Pin, Jean-Eric. (1997). Algorithms for computing
    finite semigroups. Foundations of Computational Mathematics.
    10.1007/978-3-642-60539-0_9.

The class `FroidurePin` implements the Froidure-Pin algorithm as described in
the article _Algorithms for computing finite semigroups_[^1]. If
$S = \langle G \rangle$ is a finitely generated semigroup where the elements of
$G$ can be represented as one of the element types discussed in the previous
section, then a `FroidurePin` instance can be defined on $G$, and used to answer
questions about $S$. Some questions a `FroidurePin` instance can be used to
answer (provided the algorithm terminates) include:

- What is the size of $S$?
- What are the left and right Cayley graphs of $S$?
- What is a confluent, terminating presentation for $S$.

For example, suppose that you want to work with the semigroup
$S = \langle x, y \rangle$ generated by the two bipartitions given in the
[Bipartitions](#bipartitions) section. This can be achieved in the following
way:

```python
from libsemigroups_pybind11 import Bipartition, FroidurePin
x = Bipartition([[1, -1, -2], [2, 5], [3, 4, -3], [-4, -5]])
y = Bipartition([[1, -4], [2], [3, -1], [4], [5, -3], [-2], [-5]])
S = FroidurePin([x, y])
```

Now that you have constructed `S`, you can run the Froidure-Pin algorithm. Many
of the member functions of `FroidurePin` will result in the algorithm being
started, but the most explicit way of starting the algorithm is by calling the
`run` function:

```python
S.run()
#0: FroidurePin: enumerating until all elements are found . . .
#0: FroidurePin: ⌀ 1    (Cayley graph) | 2           (elements) | 0         (rules) | 488ns   (total)
#0: FroidurePin: ⌀ 2    (Cayley graph) | 6           (elements) | 0         (rules) | 28µs    (total)
#0: FroidurePin: ⌀ 3    (Cayley graph) | 13          (elements) | 1         (rules) | 43µs    (total)
#0: FroidurePin: ⌀ 4    (Cayley graph) | 24          (elements) | 3         (rules) | 59µs    (total)
#0: FroidurePin: ⌀ 5    (Cayley graph) | 40          (elements) | 6         (rules) | 77µs    (total)
#0: FroidurePin: ⌀ 6    (Cayley graph) | 57          (elements) | 14        (rules) | 95µs    (total)
#0: FroidurePin: ⌀ 7    (Cayley graph) | 73          (elements) | 16        (rules) | 114µs   (total)
#0: FroidurePin: ⌀ 8    (Cayley graph) | 85          (elements) | 16        (rules) | 129µs   (total)
#0: FroidurePin: ⌀ 9    (Cayley graph) | 90          (elements) | 16        (rules) | 137µs   (total)
#0: FroidurePin: ⌀ 10   (Cayley graph) | 91          (elements) | 16        (rules) | 142µs   (total)
#0: FroidurePin:
#0: FroidurePin: number of products was  105 of 182 (57.692%)
```

As you can see, this resulted in some output that reports the progress of the
algorithm. In particular, looking at the third-from-last line, you can see that
the algorithm finished having enumerated $91$ elements in 142 microseconds. This
can be checked by calling `S.size()`:

```python
S.size() # returns 91

```

TODO:

1. `contains`
2. draw a cayley graph
3. mention partial enumeration?

!!! danger

    The example shown here is small, and hence `run` finished very quickly. We
    knew that the algorithm would terminate quickly because $S$ is a
    subsemigroup of the partition monoid of degree $5$, and hence has size at
    most $115,975$. In general, the size of the semigroup being enumerated is
    unknown, and therefore there is no limit on how long `run` can take to
    terminate, if at all. Therefore, it is often more practical to use the
    functions `run_for` and `run_until` in place of `run`. There are examples
    of the `run_for` function being used on the
    [Finitely presented semigroups](fp.md) page, and more information can be
    found on the [Runner class](https://libsemigroups.github.io/libsemigroups_pybind11/main-algorithms/core-classes/runner.html)
    page in the `libsemigroups_pybind11` documentation; `FroidurePin` derives
    from the `Runner` class.

### `Konieczny`
