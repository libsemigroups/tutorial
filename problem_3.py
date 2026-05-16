from libsemigroups_pybind11 import (
    Presentation,
    Congruence,
    congruence_kind,
    StringRange,
    congruence,
)

p = Presentation("abcdefg")
p.rules = ["abcd", "aaaeaa", "ef", "dg"]
p.contains_empty_word(True)

# Part (a)

c = Congruence(congruence_kind.twosided, p)
c.number_of_classes()  # returns +∞

# Part (b)


def doit():
    words = StringRange().alphabet("abcdefg").min(0).max(5)

    return congruence.partition(c, [word for i, word in enumerate(words) if i < 1000])
