# Solutions to problem 1
x := Bipartition([
    [1, 4], [2, 3], [5, -3], [6, 7], [8, -6], [9, -13], [10, 13], [11, 12],
    [14, -14], [-1, -2], [-4, -5], [-7, -12], [-8, -9], [-10, -11]
]);

# a)
J_14 := JonesMonoid(14);
Size(J_14);  # returns 2674440

# b)
Size(Idempotents(J_14));  # returns 1083028

# c)
D_x := GreensDClassOfElement(J_14, x);
Size(Idempotents(D_x));  # returns 226979

# d)
Number(Idempotents(D_x), s -> 7 in DomainOfBipartition(s));  # returns 35733
