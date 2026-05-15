# Finitely presented semigroups and monoids

This section provides information about how to compute with a finitely
presented semigroup or monoid using `libsemigroups_pybind11`.

!!! warning

    Almost every question about finitely presented semigroups and monoids is
    undecidable in general. It is

## Presentations

The algorithms in `libsemigroups_pybind11` for computing with finitely
presented semigroups and monoids all accept a `Presentation` object as (at
least part of the) input.

You can create a presentation using strings by doing:

```python
from libsemigroups_pybind11 import Presentation, presentation
p = Presentation("ab")  # a presentation with alphabet {a, b}
p.rules                 # returns the empty list
```

You can add rules to the presentation `p` all at once:

```python
p.rules = ["aba", "bbba", "babba", "a" * 10]
```

or one by one:

```python
presentation.add_rule(p, "aba", "bbba")
presentation.add_rule(p, "babba", "a" * 10)
```
