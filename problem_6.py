from libsemigroups_pybind11 import FroidurePin, word_graph, Transf, Dot, froidure_pin

s = FroidurePin([Transf([0, 0, 2]), Transf([0, 1, 1])])

# Part (a)

d = word_graph.dot(s.right_cayley_graph())
d.view()
d = word_graph.dot(s.left_cayley_graph())
d.view()
