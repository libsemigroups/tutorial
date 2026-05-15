# Worksheet

This page contains some exercises for computing some things using `libsemigroups_pybind11`.

1. Let $J_n$ denote the Jones monoid of degree $n$, and

    ![An element of the Jones monoid](../images/bipartition.png)

    be a bipartition of degree 14.

    1. How many elements does $J_{14}$ contain?
    2. How many idempotent elements does $J_{14}$ contain?
    3. How many idempotent elements does the Green's
       $\mathscr{D}$-class of $x$ in $J_{14}$ contain?
    4. How many idempotent elements $e$ such that $7$ is in the same part as 
       does the Green's $\mathscr{D}$-class of $x$ in $J_{14}$ contain?

??? hint

    You can define $J_{14}$ as a finitely presented monoid in `libsemigroups_pybind11` by doing:

    ```python
    from libsemigroups_pybind11.presentation import examples
    examples.temperley_lieb_monoid(14)
    ```
    
    You can also define the generating set returned by the following function:

    ```python
    from libsemigroups_pybind11 import Bipartition
InstallMethod(JonesMonoid, "for an integer",
[IsInt],
function(n)
  local gens, next, i, j, M;

  if n < 0 then
    ErrorNoReturn("the argument (an int) is not >= 0");
  elif n = 0 then
    return Monoid(Bipartition([]));
  elif n = 1 then
    return Monoid(Bipartition([[1, -1]]));
  fi;

  gens := [];
  for i in [1 .. n - 1] do
    next := [[i, i + 1], [-i, -i - 1]];
    for j in [1 .. i - 1] do
      Add(next, [j, -j]);
    od;
    for j in [i + 2 .. n] do
      Add(next, [j, -j]);
    od;
    Add(gens, Bipartition(next));
  od;

  M := Monoid(gens);
  SetFilterObj(M, IsRegularActingSemigroupRep);
  SetIsStarSemigroup(M, true);
  return M;
end);
    ```

