from libsemigroups_pybind11 import FroidurePin, Transf

import igraph as ig
from tqdm import tqdm

# Classes in libsemigroups_pybind11 represent particular algorithms, here we
# will use the Froidure-Pin algorithm for exhaustively enumerating the elements
# of a semigroup defined by a generating set.
#
# Transf stands for "Transformation" but is shorter.


def full_transf_monoid_generators(n: int) -> list[Transf]:
    if n == 1:
        return [Transf([0])]
    elif n == 2:
        return [Transf([1, 0]), Transf([0, 0])]

    return [
        Transf(list(range(1, n)) + [0]),
        Transf([1, 0] + list(range(2, n))),
        Transf(list(range(n - 1)) + [0]),
    ]


def commuting_graph(S: FroidurePin) -> ig.Graph:
    g = ig.Graph(S.size())

    for i in tqdm(range(S.size() - 1)):
        for j in range(i + 1, S.size()):
            if S.fast_product(i, j) == S.fast_product(j, i):
                g.add_edge(i, j)
    return g


# [
#     commuting_graph(FroidurePin(full_transf_monoid_generators(n))).clique_number()
#     for n in range(1, 6)
# ]
