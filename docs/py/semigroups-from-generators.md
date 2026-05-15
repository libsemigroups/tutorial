# Semigroups and monoids defined by generators

On [the previous page](fp.md), you saw how to construct and compute with
semigroups and monoids defined from presentations. On this page, you will learn
about presentations defined by a collection of generators. In particular, you
will learn which type of objects can be used as generators of a semigroups, and
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
