from libsemigroups_pybind11 import Bipartition, FroidurePin, Gabow


def jones_identity(n):
    if n < 0:
        raise ValueError("the argument (an int) is not >= 0")

    return Bipartition([[i, -i] for i in range(1, n + 1)])


def jones_generators(n):
    if n < 0:
        raise ValueError("the argument (an int) is not >= 0")

    gens = []
    for i in range(1, n):
        part = [[i, i + 1], [-i, -i - 1]]
        part.extend([j, -j] for j in range(1, i))
        part.extend([j, -j] for j in range(i + 2, n + 1))
        gens.append(Bipartition(part))
    return gens


def jones_monoid(n):
    return FroidurePin([jones_identity(n)] + jones_generators(n))


s = jones_monoid(14)

# Part (a)
s.size()  # returns 2674440

# Part (b)
s.number_of_idempotents()  # returns 1083028

# Part (c)
x = Bipartition(
    [
        [1, 4],
        [2, 3],
        [5, -3],
        [6, 7],
        [8, -6],
        [9, -13],
        [10, 13],
        [11, 12],
        [14, -14],
        [-1, -2],
        [-4, -5],
        [-7, -12],
        [-8, -9],
        [-10, -11],
    ]
)

# Green's relations aren't yet directly supported, so we compute the strongly
# connected components of the right and left Cayley graphs instead.

right = Gabow(s.right_cayley_graph())
left = Gabow(s.left_cayley_graph())

dclass = []
for index in right.component_of(s.position(x)):
    dclass.extend(left.component_of(index))

sum(1 for x in dclass if s.is_idempotent(x))  # returns 226979

# Part (d)

sum(1 for x in dclass if s[x].is_transverse_block(s[x][7]))  # returns 196196
