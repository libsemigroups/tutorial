S := CatalanMonoid(3);

# Part (a)

Splash(DotString(S, rec(maximal := true)));

# Part (b)
colors := List([1 .. 5], x -> ["red", "green", "blue"]);;
Splash(DotEdgeColoredDigraph(RightCayleyDigraph(S), colors));
Splash(DotEdgeColoredDigraph(LeftCayleyDigraph(S), colors));

# Part (c)

Filtered(CongruencesOfSemigroup(S), x -> not NrEquivalenceClasses(x) in [1, Size(S)] and not IsReesCongruence(x));
# returns 
# [ <2-sided semigroup congruence over <non-regular transformation monoid of size 5, degree 3 with 2 generators> with 1 generating pairs>,
#  <2-sided semigroup congruence over <non-regular transformation monoid of size 5, degree 3 with 2 generators> with 1 generating pairs> ]

# Part (d)
IsIsomorphicDigraph(LatticeOfRightCongruences(S), LatticeOfLeftCongruences(S));
# returns true

# Part (e)
M := MaximalSubsemigroups(S);
# returns [ <transformation semigroup ideal of size 4, degree 3 with 4 generators>, <transformation monoid of degree 3 with 2 generators>,
# <transformation monoid of degree 3 with 2 generators> ]
IsIsomorphicSemigroup(M[1], M[2]); # false
IsIsomorphicSemigroup(M[1], M[3]); # false
IsIsomorphicSemigroup(M[2], M[3]); # false
