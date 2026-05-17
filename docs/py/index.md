# Semigroups in Python

This part of the tutorial relates to using the functionality of
[libsemigroups][] in Python via the Python package
[libsemigroups_pybind11][].

Unlike the [Semigroups package for GAP][], [libsemigroups_pybind11][] provides
only direct low-level access to the functionality of [libsemigroups][]. This
means that [libsemigroups_pybind11][] does not provide any higher-level
constructs (like semigroups, homomorphisms, and so on), but gives fine-grained
control of the specific algorithms from [libsemigroups][]. For an overview of the
algorithms available in [libsemigroups][] and/or [libsemigroups_pybind11][], see the
[libsemigroups documentation][] or the
[libsemigroups_pybind11 documentation][].

The higher-level constructs in the Semigroups package for [GAP][] make some choices
for you about the best way to compute a particular thing. For example, if you
ask [GAP][] for the size of a finitely presented semigroup, it will run in parallel
some variants of Todd-Coxeter, Knuth-Bendix, and will try to compute the small
overlap class of the presentation. This works well in many cases, but for some
hard cases may not be enough, which is where the fine-grained control offered
by [libsemigroups_pybind11][] comes into play.

This part of this tutorial consists of:

- [Installing libsemigroups_pybind11](install.md)
- [First steps](first-steps.md)
- [Semigroups and monoids defined by generators](generated.md)
- [Finitely presented semigroups and monoids](fp.md)
- [Worksheet](worksheet.md)

[libsemigroups]: https://libsemigroups.github.io/libsemigroups/
[libsemigroups_pybind11]: https://libsemigroups.github.io/libsemigroups_pybind11/
[Semigroups package for GAP]: https://semigroups.github.io/Semigroups/
[GAP]: https://www.gap-system.org/
[libsemigroups documentation]: https://libsemigroups.github.io/libsemigroups/
[libsemigroups_pybind11 documentation]: https://libsemigroups.github.io/libsemigroups_pybind11/
