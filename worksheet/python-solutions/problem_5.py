from libsemigroups_pybind11 import (
    congruence_kind,
    ToddCoxeter,
    Sims1,
    Presentation,
    to,
    KnuthBendix,
)

p = Presentation("ab").contains_empty_word(True)
p.rules = [
    "aaaa",
    "",
    "baaaba",
    "aaabab",
    "baabaa",
    "aabaab",
    "babaaa",
    "abaaab",
    "bb",
    "b",
    "aabababab",
    "abababab",
]
tc = ToddCoxeter(congruence_kind.twosided, p)
tc.number_of_classes()  # 61

results = []
p = to(p, rtype=(Presentation, list[int]))
s = Sims1(p)
expected = [None] + [s.number_of_congruences(i) for i in range(1, 8)]

for i in range(0, len(p.rules), 2):
    q = p.copy()
    q.rules = q.rules[:i] + q.rules[i + 2 :]
    for j in range(1, 8):
        val = s.presentation(q).number_of_congruences(j)
        if val != expected[j]:
            results.append((j, val))
            break
    else:
        results.append(None)

results  #  [(2, 4), None, (4, 10), None, (2, 3), (2, 3)]

q = p.copy()
i = 2
q.rules = q.rules[:i] + q.rules[i + 2 :]
tc = ToddCoxeter(congruence_kind.twosided, q)
tc.number_of_classes()  # 61

q = p.copy()
i = 6
q.rules = q.rules[:i] + q.rules[i + 2 :]
tc = ToddCoxeter(congruence_kind.twosided, q)
tc.number_of_classes()  # 61

i = 2
q.rules = q.rules[:i] + q.rules[i + 2 :]
kb = KnuthBendix(congruence_kind.twosided, q)
kb.number_of_classes()  # +∞
