# Finitely presented semigroups and monoids

This section provides information about how to compute with a finitely
presented semigroup or monoid using the [Semigroups][] package for [GAP][].

!!! warning

    Almost every question about finitely presented semigroups and monoids is
    undecidable in general. It is easy to find examples where the algorithms
    implemented in [GAP][] will run forever, so some caution is required!

## Defining finitely presented semigroups and monoids

Let's start by defining a finitely presented semigroup in [GAP][].
Finitely presented semigroups in [GAP][] are defined as quotients of free
semigroups so let's start by creating one of these. 

!!! note
    The code examples in this section will consist of two tabs: one labelled
    "GAP REPL" showcasing the output in an example GAP REPL session, and
    another labelled "GAP script" which contains the same code without the
    GAP REPL output, for easier copy-pasting into a GAP session.

=== "GAP REPL"
    ```gap-repl
    gap> F := FreeSemigroup("a", "b");
    <free semigroup on the generators [ a, b ]>
    ```
=== "GAP script"
    ```gap
    F := FreeSemigroup("a", "b");
    ```

We've defined a free semigroup with generators named `a` and `b`. We can
access these generators by doing:

=== "GAP REPL"
    ```gap-repl
    gap> GeneratorsOfSemigroup(F);
    [ a, b ]
    ```
=== "GAP script"
    ```gap
    GeneratorsOfSemigroup(F);
    ```

This is a bit cumbersome, there's a better way:

=== "GAP REPL"
    ```gap-repl
    gap> F.1; # the first generator
    a
    gap> F.2; # the second generator
    b
    ```
=== "GAP script"
    ```gap
    F.1;
    F.2;
    ```

That's better but not great, why can't we just use the original names `a` and
`b`. We can't do this automatically because [GAP][] is rightly protecting us
from accidentally overwriting some existing variables named `a` and `b`. We can
do it explicitly though by doing:

=== "GAP REPL"
    ```gap-repl
    gap> AssignGeneratorVariables(F);
    #I  Assigned the global variables [ a, b ]
    gap> a;
    a
    gap> b;
    b
    gap> a in F;
    true
    gap> a * b * a ^ 10;
    a*b*a^10
    ```
=== "GAP script"
    ```gap
    AssignGeneratorVariables(F);
    a;
    b;
    a in F;
    a * b * a ^ 10;
    ```

You can also define a free semigroup or monoid by specifying the number of
generators, the generators are then called `s1`, `s2`, and so on for free
semigroups, and `m1`, `m2`, and so on for free monoids.

=== "GAP REPL"
    ```gap-repl
    gap> F := FreeSemigroup(10);
    <free semigroup on the generators [ s1, s2, s3, s4, s5, s6, s7, s8, s9, s10 ]>
    gap> F := FreeMonoid(10);
    <free monoid on the generators [ m1, m2, m3, m4, m5, m6, m7, m8, m9, m10 ]>
    ```
=== "GAP script"
    ```gap
    F := FreeSemigroup(10);
    F := FreeMonoid(10);
    ```

Now we have (probably) the most convenient way of using the generators, to
define some relations. These are just lists consisting of products of the
generators of `F`:

=== "GAP REPL"
    ```gap-repl
    gap> F := FreeMonoid("b", "y", "r");;
    gap> AssignGeneratorVariables(F);
    #I  Global variable `b' is already defined and will be overwritten
    #I  Assigned the global variables [ b, y, r ]
    gap> R := [[b * y * r, b], [y * r * b, y], [r * b * y, r]];
    [ [ b*y*r, b ], [ y*r*b, y ], [ r*b*y, r ] ]
    gap> M := F / R;
    <fp monoid with 3 generators and 3 relations of length 15>
    gap> Size(M);
    7
    gap> Elements(M);
    [ <identity ...>, b, b^2, y, y*b, r, r*b ]
    ```
=== "GAP script"
    ```gap
    F := FreeMonoid("b", "y", "r");;
    AssignGeneratorVariables(F);
    R := [[b * y * r, b], [y * r * b, y], [r * b * y, r]];
    M := F / R;
    Size(M);
    Elements(M);
    ```

This works pretty well if the presentation you are trying to define is small
and not very complicated. Here's another way using [ParseRelations][]:

=== "GAP REPL"
    ```gap-repl
    gap> F := FreeSemigroup("x", "y", "z");;
    gap> R := ParseRelations(GeneratorsOfSemigroup(F), "x=(y^2z)^2x, y=x^3, z=y^3");
    [ [ x, (y^2*z)^2*x ], [ y, x^3 ], [ z, y^3 ] ]
    gap> S := F / R;
    <fp semigroup with 3 generators and 3 relations of length 19>
    gap> Size(S);
    30
    ```
=== "GAP script"
    ```gap
    F := FreeSemigroup("x", "y", "z");;
    R := ParseRelations(GeneratorsOfSemigroup(F), "x=(y^2z)^2x, y=x^3, z=y^3");
    S := F / R;
    Size(S);
    ```

[ParseRelations]: https://semigroups.github.io/Semigroups/doc/chap15_mj.html#X7C2FCCA487DFC84C

??? tip 

    Every free semigroup created using [FreeSemigroup][] is a distinct
    entity in [GAP][], this can be a bit surprising at first:

    === "GAP REPL"
        ```gap-repl
        gap> F1 := FreeSemigroup("x", "y", "z");;
        gap> F2 := FreeSemigroup("x", "y", "z");;
        gap> F1 = F2;
        false
        ```
    === "GAP script"
        ```gap
        F1 := FreeSemigroup("x", "y", "z");;
        F2 := FreeSemigroup("x", "y", "z");;
        F1 = F2;
        ```

    Arguably `F1` and `F2` are equal but in [GAP][] they are not (mostly for
    technical reasons). The same behaviour happens for [FreeMonoid][] too. It's
    a fairly common abuse (of notation?) for people to identify elements of a free
    semigroups and monoids with elements of the finitely presented semigroup or
    monoid they are interested in. In [GAP][] you cannot do this, the elements of a
    finitely presented semigroup (or monoid) and the free semigroup (or monoid)
    over which they are defined are separate:

    === "GAP REPL"
        ```gap-repl
        gap> F := FreeSemigroup("x", "y", "z");;
        gap> R := ParseRelations(GeneratorsOfSemigroup(F), "x=(y^2z)^2x, y=x^3, z=y^3");
        [ [ x, (y^2*z)^2*x ], [ y, x^3 ], [ z, y^3 ] ]
        gap> S := F / R;
        <fp semigroup with 3 generators and 3 relations of length 19>
        gap> F.1 in S;
        false
        gap> S.1 in F;
        false
        ```
    === "GAP script"
        ```gap
        F := FreeSemigroup("x", "y", "z");;
        R := ParseRelations(GeneratorsOfSemigroup(F), "x=(y^2z)^2x, y=x^3, z=y^3");
        S := F / R;
        F.1 in S;
        S.1 in F;
        ```

## Finitely presented groups vs semigroups and monoids in [GAP][]

You might be thinking that there must be lots of fancy group specific
algorithms for computing finitely presented groups. You'd be correct, to some
extent, at least. You might also be surprised to learn that the
performance of the implementations in the [Semigroups][] package for [GAP][]
(which use [libsemigroups][]) is often much much better than the performance of
the group specific algorithms in the main [GAP][] library.  Here are some
examples.

The following defines the symmetric group on 12 points using Moore's
presentation from:

* E. H. Moore. Concerning the abstract groups of order k!, k!/2, *Proc. London Math. Soc.*, **28** 357–366, 1897.

=== "GAP REPL"
    ```gap-repl
    gap> F := FreeGroup(11);;
    gap> R := [];;
    gap> for i in [1 .. 11] do
    >      Add(R, [F.(i) ^ 2, One(F)]);
    >    od;
    gap> for i in [1 .. 10] do
    >      Add(R, [F.(i) * F.(i + 1) * F.(i), F.(i + 1) * F.(i) * F.(i + 1)]);
    >    od;
    gap> for i in [1 .. 9] do
    >      for j in [i + 2 .. 11] do
    >        Add(R, [F.(i) * F.(j), F.(j) * F.(i)]);
    >      od;
    >    od;
    gap>       G := F / R;
    <fp group on the generators [ f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11 ]>
    gap>       Size(G);
    ^CError, user interrupt  # runs for a long long time
    gap> M := Range(IsomorphismFpMonoid(G));
    <fp monoid with 22 generators and 88 relations of length 328>
    gap> Size(M);  # takes approximately 3 milliseconds . . .
    479001600 
    ```
=== "GAP script"
    ```gap
    F := FreeGroup(11);;
    R := [];;
    for i in [1 .. 11] do
      Add(R, [F.(i) ^ 2, One(F)]);
    od;
    for i in [1 .. 10] do
      Add(R, [F.(i) * F.(i + 1) * F.(i), F.(i + 1) * F.(i) * F.(i + 1)]);
    od;
    for i in [1 .. 9] do
      for j in [i + 2 .. 11] do
        Add(R, [F.(i) * F.(j), F.(j) * F.(i)]);
      od;
    od;
    G := F / R;
    Size(G);
    M := Range(IsomorphismFpMonoid(G));
    Size(M);
    ```

Here's another example:

=== "GAP REPL"
    ```gap-repl
    gap> F := FreeGroup(2);; f1 := F.1;; f2 := F.2;;
    gap> G := F / [ f2 ^ 100, f1 ^ 2, f2 * f1 * f2 ^ -99 * f1 ^ -1 ];;
    gap> Size(G);  # takes about 1.7 seconds on my computer
    200
    gap> M := Range(IsomorphismFpMonoid(G));
    <fp monoid with 4 generators and 7 relations of length 216>
    gap> Size(M);  # takes about 1 millisecond
    200
    ```
=== "GAP script"
    ```gap
    F := FreeGroup(2);; f1 := F.1;; f2 := F.2;;
    G := F / [ f2 ^ 100, f1 ^ 2, f2 * f1 * f2 ^ -99 * f1 ^ -1 ];;
    Size(G);
    M := Range(IsomorphismFpMonoid(G));
    Size(M);
    ```

Here's another example:

=== "GAP REPL"
    ```gap-repl

    gap> F := FreeGroup(2);;
    gap> gen := GeneratorsOfGroup(F);;
    gap> a := gen[1];; b := gen[2];;
    gap> g := F / [a^120, b^4, a*b*(b^3*a^41)^-1, a^2*b*(b*a^82)^-1];
    <fp group on the generators [ f1, f2 ]>
    gap> IsomorphismPermGroup(g); # this is quite fast
    [ f1, f2 ] -> [ (1,2,3,4,5)(6,7,9,11,8,10,12,13)(14,15,16)(18,19),
      (6,8)(7,10)(9,12)(11,13)(15,16)(17,18,20,19) ]
    gap> s:= Range(IsomorphismFpSemigroup(g));
    <fp semigroup with 5 generators and 17 relations of length 304>
    gap> IsomorphismTransformationSemigroup(s); # so is this
    <fp semigroup with 5 generators and 17 relations of length 304> ->
    <transformation monoid of size 480, degree 480 with 4 generators>
    gap> IsomorphismPermGroup(Range(last));
    <transformation group of size 480, degree 480 with 4 generators> ->
    <permutation group of size 480 with 5 generators>
    ```

=== "GAP script"
    ```gap
    F := FreeGroup(2);;
    gen := GeneratorsOfGroup(F);;
    a := gen[1];; b := gen[2];;
    g := F / [a^120, b^4, a*b*(b^3*a^41)^-1, a^2*b*(b*a^82)^-1];
    IsomorphismPermGroup(g); # this is quite fast
    s:= Range(IsomorphismFpSemigroup(g));
    IsomorphismTransformationSemigroup(s);
    IsomorphismPermGroup(Range(last));
    ```

!!! danger 

    At this point I should admit that the examples in this section were
    specially selected to show [Semigroups][] in its best light, and the [GAP][]
    library in its worst. A fairer comparison would have been to include some other
    examples where [GAP][] is better than [Semigroups][], or where other tools
    (like [ACE][] or [kbmag][]) are faster as well. The truth is that any software
    for computing with finitely presented semigroups, monoids or groups, has its
    limitations and given the undecidable nature of most related problems, it is
    always possible to contrive examples which are hard or impossible for any
    particular implementation to handle.  

## Finite or infinite?

In [GAP][] there's only really a single way to check if a finitely presented
semigroup or monoid is finite or infinite:

=== "GAP REPL"
    ```gap-repl
    gap> F := FreeSemigroup("a", "b", "c", "d");
    <free semigroup on the generators [ a, b, c, d ]>
    gap> R := ParseRelations(GeneratorsOfSemigroup(F),
    >            "(ab)^4=a,b^7=b^2,c^4=c,d^5=d^2,cd=dc");
    [ [ (a*b)^4, a ], [ b^7, b^2 ], [ c^4, c ], [ d^5, d^2 ], [ c*d, d*c ] ]
    gap> IsFinite(F / R);
    false
    gap> Size(F / R);
    infinity
    ```

=== "GAP script"
    ```gap
    F := FreeSemigroup("a", "b", "c", "d");
    R := ParseRelations(GeneratorsOfSemigroup(F), 
           "(ab)^4=a,b^7=b^2,c^4=c,d^5=d^2,cd=dc");
    IsFinite(F / R);
    Size(F / R);
    ```

This will work when any of the conditions described [here](https://libsemigroups.github.io/libsemigroups_pybind11/data-structures/presentations/obvinf.html) are satisfied,
if `F / R` has small overlap class at least $3$, or if it is possible to
compute a complete rewriting system for `F / R`.

=== "GAP REPL"
    ```gap-repl
    gap> F := FreeSemigroup("a", "b", "c");
    <free semigroup on the generators [ a, b, c ]>
    gap> AssignGeneratorVariables(F);
    #I  Assigned the global variables [ a, b, c ]
    gap> R := ParseRelations([a, b, c], "aabc=acba");
    [ [ a^2*b*c, a*c*b*a ] ]
    gap> IsFinite(F / R);
    false
    ```

=== "GAP script"
    ```gap
    F := FreeSemigroup("a", "b", "c");
    AssignGeneratorVariables(F);
    R := ParseRelations([a, b, c], "aabc=acba");
    IsFinite(F / R);
    ```

## Non-isomorphism

In this section we show how to demonstrate that two monoids or semigroups
defined by presentations are not isomorphic.

The following is Shutov's presentation for the symmetric inverse monoid of
degree $4$ from:

* É. G. Shutov, Defining relations in finite semigroups of partial transformations, *Sov. Math., Dokl.* 1:784–786, 1960.

=== "GAP REPL"
    ```gap-repl
    gap> F := FreeMonoid("a", "b", "c", "e");
    <free monoid on the generators [ a, b, c, e ]>
    gap> R := ParseRelations(GeneratorsOfMonoid(F),
    > "aa=1, bb=1, cc=1, (ab)^3=1, (bc)^3=1, (ca)^3=1, (abac)^2=1, (bcba)^2=1, (cacb)^2=1, \
    ee=e, eaea=aeae, aeab=baea, beba=abeb, aeac=caea, ceca=acec, aeaea=aeae");
    [ [ a^2, <identity ...> ], [ b^2, <identity ...> ], [ c^2, <identity ...> ],
      [ (a*b)^3, <identity ...> ], [ (b*c)^3, <identity ...> ], [ (c*a)^3, <identity ...> ],
      [ (a*b*a*c)^2, <identity ...> ], [ (b*c*b*a)^2, <identity ...> ],
      [ (c*a*c*b)^2, <identity ...> ], [ e^2, e ], [ (e*a)^2, (a*e)^2 ],
      [ a*e*a*b, b*a*e*a ], [ b*e*b*a, a*b*e*b ], [ a*e*a*c, c*a*e*a ],
      [ c*e*c*a, a*c*e*c ], [ (a*e)^2*a, (a*e)^2 ] ]
    gap> M := F / R;
    <fp monoid with 4 generators and 16 relations of length 104>
    gap> Size(M);
    209
    ```

=== "GAP script"
    ```gap
    F := FreeMonoid("a", "b", "c", "e");
    R := ParseRelations(GeneratorsOfMonoid(F),
    "aa=1, bb=1, cc=1, (ab)^3=1, (bc)^3=1, (ca)^3=1, (abac)^2=1, (bcba)^2=1, (cacb)^2=1, \
    ee=e, eaea=aeae, aeab=baea, beba=abeb, aeac=caea, ceca=acec, aeaea=aeae");
    M := F / R;
    Size(M);
    ```

Let's check if the monoid defined by all but the last relation $aeaea=aeae$ in
`R` defines the symmetric inverse monoid on 4 points also. One way of doing
this is to just remove the relation, and check if the presentation defines a
monoid of the same size. This sometimes works, and it does here:

=== "GAP REPL"
    ```gap-repl
    gap> F := FreeMonoid("a", "b", "c", "e");;
    gap> R := ParseRelations(GeneratorsOfMonoid(F),
    > "aa=1, bb=1, cc=1, (ab)^3=1, (bc)^3=1, (ca)^3=1, (abac)^2=1, (bcba)^2=1,
    > (cacb)^2=1, aeaea=aeae");
    [ [ a^2, <identity ...> ], [ b^2, <identity ...> ], [ c^2, <identity ...> ],
      [ (a*b)^3, <identity ...> ], [ (b*c)^3, <identity ...> ], [ (c*a)^3,
    <identity ...> ],
      [ (a*b*a*c)^2, <identity ...> ], [ (b*c*b*a)^2, <identity ...> ],
      [ (c*a*c*b)^2, <identity ...> ], [ e^2, e ], [ (e*a)^2, (a*e)^2 ],
      [ a*e*a*b, b*a*e*a ], [ b*e*b*a, a*b*e*b ], [ a*e*a*c, c*a*e*a ],
      [ c*e*c*a, a*c*e*c ], [ (a*e)^2*a, (a*e)^2 ] ]
    gap> Remove(R, Length(R));
    [ (a*e)^2*a, (a*e)^2 ]
    gap> M := F / R;
    <fp monoid with 4 generators and 15 relations of length 95>
    gap> Size(M);
    384
    ```

=== "GAP script"
    ```gap
    F := FreeMonoid("a", "b", "c", "e");;
    R := ParseRelations(GeneratorsOfMonoid(F),
    "aa=1, bb=1, cc=1, (ab)^3=1, (bc)^3=1, (ca)^3=1, (abac)^2=1, (bcba)^2=1, (cacb)^2=1, \
    ee=e, eaea=aeae, aeab=baea, beba=abeb, aeac=caea, ceca=acec, aeaea=aeae");
    Remove(R, Length(R));
    M := F / R;
    Size(M);
    ```

so the last relation is not redundant!

Let's try again with the second to last relation $ceca=acec$.

=== "GAP REPL"
    ```gap-repl
    gap> F := FreeMonoid("a", "b", "c", "e");;
    gap> R := ParseRelations(GeneratorsOfMonoid(F),
    > "aa=1, bb=1, cc=1, (ab)^3=1, (bc)^3=1, (ca)^3=1, (abac)^2=1, (bcba)^2=1,
    > (cacb)^2=1, ee=e, eaea=aeae, aeab=baea, beba=abeb, aeac=caea, ceca=acec,
    > aeaea=aeae");
    [ [ a^2, <identity ...> ], [ b^2, <identity ...> ], [ c^2, <identity ...> ],
      [ (a*b)^3, <identity ...> ], [ (b*c)^3, <identity ...> ], [ (c*a)^3,
    <identity ...> ],
      [ (a*b*a*c)^2, <identity ...> ], [ (b*c*b*a)^2, <identity ...> ],
      [ (c*a*c*b)^2, <identity ...> ], [ e^2, e ], [ (e*a)^2, (a*e)^2 ],
      [ a*e*a*b, b*a*e*a ], [ b*e*b*a, a*b*e*b ], [ a*e*a*c, c*a*e*a ],
      [ c*e*c*a, a*c*e*c ], [ (a*e)^2*a, (a*e)^2 ] ]
    gap> Remove(R, Length(R) - 1);
    [ c*e*c*a, a*c*e*c ]
    gap> M := F / R;
    <fp monoid with 4 generators and 15 relations of length 96>
    gap> Size(M);
    209
    ```

=== "GAP script"
    ```gap
    F := FreeMonoid("a", "b", "c", "e");;
    R := ParseRelations(GeneratorsOfMonoid(F),
    "aa=1, bb=1, cc=1, (ab)^3=1, (bc)^3=1, (ca)^3=1, (abac)^2=1, (bcba)^2=1, (cacb)^2=1, \
    ee=e, eaea=aeae, aeab=baea, beba=abeb, aeac=caea, ceca=acec, aeaea=aeae");
    Remove(R, Length(R) - 1);
    M := F / R;
    Size(M);
    ```

So the second to last relation is redundant. Let's try again with the relation
$eaea=aeae$ which is `R[11]`:

=== "GAP REPL"
    ```gap-repl
    gap>     F := FreeMonoid("a", "b", "c", "e");;
    gap>     R := ParseRelations(GeneratorsOfMonoid(F),
    >     "aa=1, bb=1, cc=1, (ab)^3=1, (bc)^3=1, (ca)^3=1, (abac)^2=1, (bcba)^2=1, (cacb)^2=1, \
    >     ee=e, eaea=aeae, aeab=baea, beba=abeb, aeac=caea, ceca=acec, aeaea=aeae");
    [ [ a^2, <identity ...> ], [ b^2, <identity ...> ], [ c^2, <identity ...> ],
      [ (a*b)^3, <identity ...> ], [ (b*c)^3, <identity ...> ], [ (c*a)^3, <identity ...> ],
      [ (a*b*a*c)^2, <identity ...> ], [ (b*c*b*a)^2, <identity ...> ],
      [ (c*a*c*b)^2, <identity ...> ], [ e^2, e ], [ (e*a)^2, (a*e)^2 ],
      [ a*e*a*b, b*a*e*a ], [ b*e*b*a, a*b*e*b ], [ a*e*a*c, c*a*e*a ],
      [ c*e*c*a, a*c*e*c ], [ (a*e)^2*a, (a*e)^2 ] ]
    gap>     Remove(R, 11);
    [ (e*a)^2, (a*e)^2 ]
    gap>     M := F / R;
    <fp monoid with 4 generators and 15 relations of length 96>
    gap>     Size(M);
    384
    ```

=== "GAP script"
    ```gap
    F := FreeMonoid("a", "b", "c", "e");;
    R := ParseRelations(GeneratorsOfMonoid(F),
    "aa=1, bb=1, cc=1, (ab)^3=1, (bc)^3=1, (ca)^3=1, (abac)^2=1, (bcba)^2=1, (cacb)^2=1, \
    ee=e, eaea=aeae, aeab=baea, beba=abeb, aeac=caea, ceca=acec, aeaea=aeae");
    Remove(R, 11);
    M := F / R;
    Size(M);
    ```

So $eaea=aeae$ is also not redundant. Let's try again with the
first rule `a^2=1`.

=== "GAP REPL"
    ```gap-repl
    gap> F := FreeMonoid("a", "b", "c", "e");;
    gap> R := ParseRelations(GeneratorsOfMonoid(F),
    > "bb=1, cc=1, (ab)^3=1, (bc)^3=1, (ca)^3=1, (abac)^2=1, (bcba)^2=1,
    > (cacb)^2=1, \
    > ee=e, eaea=aeae, aeab=baea, beba=abeb, aeac=caea, ceca=acec,
    > aeaea=aeae");
    [ [ b^2, <identity ...> ], [ c^2, <identity ...> ], [ (a*b)^3, <identity ...>
    ],
      [ (b*c)^3, <identity ...> ], [ (c*a)^3, <identity ...> ],
      [ (a*b*a*c)^2, <identity ...> ], [ (b*c*b*a)^2, <identity ...> ],
      [ (c*a*c*b)^2, <identity ...> ], [ e^2, e ], [ (e*a)^2, (a*e)^2 ],
      [ a*e*a*b, b*a*e*a ], [ b*e*b*a, a*b*e*b ], [ a*e*a*c, c*a*e*a ],
      [ c*e*c*a, a*c*e*c ], [ (a*e)^2*a, (a*e)^2 ] ]
    gap> M := F / R;
    <fp monoid with 4 generators and 15 relations of length 102>
    ```

=== "GAP script"
    ```gap
    F := FreeMonoid("a", "b", "c", "e");;
    R := ParseRelations(GeneratorsOfMonoid(F),
    "bb=1, cc=1, (ab)^3=1, (bc)^3=1, (ca)^3=1, (abac)^2=1, (bcba)^2=1, (cacb)^2=1, \
    ee=e, eaea=aeae, aeab=baea, beba=abeb, aeac=caea, ceca=acec, aeaea=aeae");
    M := F / R;
    ```

If we would try doing `Size(M)`, then it'd just run for a long time with no
output. So this is inconclusive. Maybe it's infinite but we just can't tell
this easily using the computer.

The [low-index congruence
algorithm](https://pubs.ams.org/journals/mcom/0000-000-00/S0025-5718-2025-04136-X)
(similar to Sims' low index subgroup algorithm) can compute the numbers of
left/right congruences on a finitely presented semigroup or monoid,
regardless of whether or not it is finite. This algorithm is
what is behind
[NumberOfRightCongruences](https://semigroups.github.io/Semigroups/doc/chap13_mj.html#X7AE16F237E862934).
The following computes the number of right congruences with up to 5
classes on the monoid defined by the presentation for the symmetric inverse
monoid with the relation $a^2 = 1$ removed:

=== "GAP REPL"
    ```gap-repl
    gap> F := FreeMonoid("a", "b", "c", "e");;
    gap> R := ParseRelations(GeneratorsOfMonoid(F),
    > "bb=1, cc=1, (ab)^3=1, (bc)^3=1, (ca)^3=1, (abac)^2=1, (bcba)^2=1, (cacb)^2=1, \
    > ee=e, eaea=aeae, aeab=baea, beba=abeb, aeac=caea, ceca=acec, aeaea=aeae");
    [ [ b^2, <identity ...> ], [ c^2, <identity ...> ], [ (a*b)^3, <identity ...> ],
      [ (b*c)^3, <identity ...> ], [ (c*a)^3, <identity ...> ],
      [ (a*b*a*c)^2, <identity ...> ], [ (b*c*b*a)^2, <identity ...> ],
      [ (c*a*c*b)^2, <identity ...> ], [ e^2, e ], [ (e*a)^2, (a*e)^2 ],
      [ a*e*a*b, b*a*e*a ], [ b*e*b*a, a*b*e*b ], [ a*e*a*c, c*a*e*a ],
      [ c*e*c*a, a*c*e*c ], [ (a*e)^2*a, (a*e)^2 ] ]
    gap> M := F / R;
    <fp monoid with 4 generators and 15 relations of length 102>
    gap> NumberOfRightCongruences(M, 5);
    26
    gap> NumberOfRightCongruences(SymmetricInverseMonoid(4), 5);
    18
    ```

=== "GAP script"
    ```gap
    F := FreeMonoid("a", "b", "c", "e");;
    R := ParseRelations(GeneratorsOfMonoid(F),
    "bb=1, cc=1, (ab)^3=1, (bc)^3=1, (ca)^3=1, (abac)^2=1, (bcba)^2=1, (cacb)^2=1, \
    ee=e, eaea=aeae, aeab=baea, beba=abeb, aeac=caea, ceca=acec, aeaea=aeae");
    M := F / R;
    NumberOfRightCongruences(M, 5);
    NumberOfRightCongruences(SymmetricInverseMonoid(4), 5);
    ```
This says that the symmetric inverse monoid has 18 right congruences with up to
5 classes, but the monoid defined by the presentation with the first relation
removed has 26 such congruences. So, these monoids are not isomorphic, and so
the relation $a^2=1$ is not redundant.

[libsemigroups]: https://libsemigroups.github.io/libsemigroups/
[GAP]: https://gap-system.org
[Semigroups]: https://semigroups.github.io/Semigroups/
[ACE]: https://gap-packages.github.io/ace/
[KBMAG]: https://gap-packages.github.io/kbmag/
[FreeSemigroup]: https://docs.gap-system.org/doc/ref/chap51_mj.html#X7C72E4747BF642BB
[FreeMonoid]: https://docs.gap-system.org/doc/ref/chap51_mj.html#X79FA3FA978CA2E43
