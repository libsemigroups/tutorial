from libsemigroups_pybind11.presentation import examples
from libsemigroups_pybind11 import ToddCoxeter, congruence_kind, Sims1

p = examples.not_symmetric_group(4)
tc = ToddCoxeter(congruence_kind.twosided, p)
tc.number_of_classes()  # returns 72

p = examples.not_symmetric_group(5)
Sims1(p).number_of_congruences(3)  # returns 41
q = examples.symmetric_group(5)
Sims1(q).number_of_congruences(3)  # returns 2

p = examples.not_symmetric_group(6)
Sims1(p).number_of_congruences(3)  # returns 122
q = examples.symmetric_group(5)
Sims1(q).number_of_congruences(3)  # returns 2

p = examples.not_symmetric_group(7)
Sims1(p).number_of_congruences(3)  # returns 365
q = examples.symmetric_group(7)
Sims1(q).number_of_congruences(3)  # returns 2

p = examples.not_symmetric_group(8)
Sims1(p).number_of_congruences(3)  # returns 1094
q = examples.symmetric_group(8)
Sims1(q).number_of_congruences(3)  # returns 2
