F := FreeMonoid("a", "b");
AssignGeneratorVariables(F);;
R := [
          [a * a * a * a, One(F)],
          [b * a * a * a * b * a, a * a * a * b * a * b],
          [b * a * a * b * a * a, a * a * b * a * a * b],
          [b * a * b * a * a * a, a * b * a * a * a * b],
          [b * b, b],
          [a * a * b * a * b * a * b * a * b, a * b * a * b * a * b * a * b]
         ];
S := F / R;
T := [];
Size(S); # returns 61

results := [];
expected := List([1 .. 8], x -> NumberOfRightCongruences(S, x));

for i in [1 .. Length(R)] do
  RR := ShallowCopy(R);
  Remove(RR, i);
  Add(T, F / RR);
  found := false;
  for j in [1 .. 8] do
    val := NumberOfRightCongruences(F / RR, j);
    if val <> expected[j] then
      Add(results, [j, val]);
      found := true;
      break;
    fi;
  od;
  if not found then
    Add(results, fail);
  fi;
od;

PositionsProperty(results, x -> x <> fail); # [1, 3, 5, 6] are hence irredundant
List(T{Positions(results, fail)}, Size); # [ 61, 61] 
# and so the other relations are redundant

# Remove both redundant relations now
Remove(R, 4);
Remove(R, 2);

Size(F / R); # infinity!

# So removing either rule 2 or 4 yields the minimal set of relations required.
