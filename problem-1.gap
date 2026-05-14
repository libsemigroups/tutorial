# Solutions to problem 1
x := Bipartition([
    [1, 4], [2, 3], [5, -3], [6, 7], [8, -6], [9, -13], [10, 13], [11, 12],
    [14, -14], [-1, -2], [-4, -5], [-7, -12], [-8, -9], [-10, -11]
]);;

# a)
Irreducibles := IrreducibleComponentsOfBipartition(x);;
Size(Irreducibles);  # returns 3

# b)
J_14 := JonesMonoid(14);;
Size(J_14);  # returns 2674440

# c)
JonesIdempotents := Idempotents(J_14);;
Size(JonesIdempotents);  # returns 1083028

# # c) much slower alternative
# Number(J_14, IsIdempotent);  # returns 1083028

# d)
D_x               := GreensDClassOfElement(J_14, x);;
DClassIdempotents := Idempotents(D_x);;
Size(DClassIdempotents);  # returns 226979

# e)
Number(DClassIdempotents, s -> 7 in DomainOfBipartition(s));  # returns 35733

# f)
Number(
    DClassIdempotents,
    s -> (7 in DomainOfBipartition(s)) and IsIrreducibleBipartition(s)
);  # returns 6