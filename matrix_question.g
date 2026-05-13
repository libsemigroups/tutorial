gens := [ 
    Matrix(IsMaxPlusMatrix, 
    [
        [0, -infinity, -infinity, -infinity, 1],
        [-infinity, 0, -infinity, -infinity, 1],
        [-infinity, -infinity, 0, -infinity, 1],
        [-infinity, -infinity, -infinity, -infinity, 1], 
        [-infinity, -infinity, -infinity, -infinity, 0]]), 
    Matrix(IsMaxPlusMatrix,
    [
        [0, -infinity, -infinity, 1, 1],
        [-infinity, 0, -infinity, 1, 1],
        [-infinity, -infinity, 0, 1, 1], 
        [-infinity, -infinity, -infinity, 0, -infinity],
        [-infinity, -infinity, -infinity, -infinity, 0]]), 
    Matrix(IsMaxPlusMatrix,
    [
        [0, -infinity, 1, 1, 1],
        [-infinity, 0, 1, 1, 1],
        [-infinity, -infinity, 0, -infinity, -infinity], 
        [-infinity, -infinity, -infinity, 0, -infinity],
        [-infinity, -infinity, -infinity, -infinity, 0]]), 
  Matrix(IsMaxPlusMatrix,
    [
        [0, 1, 1, 1, 1],
        [-infinity, 0, -infinity, -infinity, -infinity],
        [-infinity, -infinity, 0, -infinity, -infinity], 
        [-infinity, -infinity, -infinity, 0, -infinity],
        [-infinity, -infinity, -infinity, -infinity, 0]])
];

# gap> Display(gens);
#  0 -∞ -∞ -∞  1
# -∞  0 -∞ -∞  1
# -∞ -∞  0 -∞  1
# -∞ -∞ -∞ -∞  1
# -∞ -∞ -∞ -∞  0

#  0 -∞ -∞  1  1
# -∞  0 -∞  1  1
# -∞ -∞  0  1  1
# -∞ -∞ -∞  0 -∞
# -∞ -∞ -∞ -∞  0

#  0 -∞  1  1  1
# -∞  0  1  1  1
# -∞ -∞  0 -∞ -∞
# -∞ -∞ -∞  0 -∞
# -∞ -∞ -∞ -∞  0

#  0  1  1  1  1
# -∞  0 -∞ -∞ -∞
# -∞ -∞  0 -∞ -∞
# -∞ -∞ -∞  0 -∞
# -∞ -∞ -∞ -∞  0

S := Semigroup(gens);

F := FreeMonoid("a", "b", "c", "d");
AssignGeneratorVariables(F);;
R := [
          [b * a * c, b * c * a],
          [a * c * b, c * a * b],
          [b * a * d, b * d * a],
          [a * d * b, d * a * b],
          [c * a * d, c * d * a],
          [a * d * c, d * a * c],
          [c * b * d, c * d * b],
          [b * d * c, d * b * c],
          [b * a * a, a * b * a],
          [b * b * a, b * a * b],
          [c * a * a, a * c * a],
          [c * c * a, c * a * c],
          [c * b * b, b * c * b],
          [c * c * b, c * b * c],
          [d * a * a, a * d * a],
          [d * d * a, d * a * d],
          [d * b * b, b * d * b],
          [d * d * b, d * b * d],
          [d * c * c, c * d * c],
          [d * d * c, d * c * d],
          [a * a, a],
          [b * b, b],
          [c * c, c],
          [d * d, d]
         ];
Sty4 := F / R;

Size(S);
Size(Sty4);