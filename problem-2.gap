# Solution to problem 2

S := FullTransformationMonoid(2);
D := Digraph(Elements(S), {x, y} -> x * y = y * x);
CliqueNumber(D); # returns 2

S := FullTransformationMonoid(3);
D := Digraph(Elements(S), {x, y} -> x * y = y * x);
CliqueNumber(D); # returns 4

S := FullTransformationMonoid(4);
D := Digraph(Elements(S), {x, y} -> x * y = y * x);
CliqueNumber(D); # returns 8

S := FullTransformationMonoid(5);
D := Digraph(Elements(S), {x, y} -> x * y = y * x);
CliqueNumber(D); # returns 16 (although it takes a while)
