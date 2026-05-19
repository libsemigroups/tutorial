# Worksheet


This worksheet contains some exercises to be completed in [GAP][] with the use
of the [Semigroups package for GAP][] package as part of the [GAP][] workshop
session of [NBSAN 40](https://manchester-semigroups.github.io/NBSAN/next.html). 

1.  Let $J_n$ denote the Jones monoid of degree $n$, and
    ![An element of the Jones monoid](../images/bipartition.png)

    1.  Find a collection of bipartitions $\{x_1, x_2, \dots, x_j\}$ such that
        the tensor product $x_1 \otimes x_2 \otimes \dots \otimes x_j$ is equal
    to $x$. What is the largest possible value of $j$? For the definition of
    the tensor product of bipartitions, see the documentation of the function
    [`TensorBipartition`](https://semigroups.github.io/Semigroups/doc/chap3_mj.html#X7F7D823084F79C7D).

    2.  How many elements does $J_{14}$ contain?

    3.  How many idempotent elements does $J_{14}$ contain?

    4.  How many idempotent elements does the Green's
        $\mathscr{D}$-class of $x$ in $J_{14}$ contain?

    5.  How many idempotent elements $e$ such that $7$ belongs to the same part
        as a negative number does the Green's $\mathscr{D}$-class of $x$ in
        $J_{14}$ contain?

    6.  Same question as the previous part but for *irreducible* idempotents
        instead.

        ??? hint
            
            You might find the following functions helpful:

            * [`DClass`](https://semigroups.github.io/Semigroups/doc/chap10_mj.html#X81B7AD4C7C552867)
            * [`DomainOfBipartition`](https://semigroups.github.io/Semigroups/doc/chap3_mj.html#X8657EE2B79E1DD02)
            * [`IsIrreducibleIdempotent`](https://semigroups.github.io/Semigroups/doc/chap3_mj.html#X78999D6F8231AE79)
            * [`JonesMonoid`](https://semigroups.github.io/Semigroups/doc/chap7_mj.html#X8378FC8B840B9706)
            * [`NrIdempotents`](https://semigroups.github.io/Semigroups/doc/chap11_mj.html#X7CFC4DB387452320)
            * [`Size`](https://docs.gap-system.org/doc/ref/chap30_mj.html#X858ADA3B7A684421)

2.  Recall that the commuting graph of a semigroup $S$ is the graph with
    nodes the elements of $S$ and an edge $(x, y)$ if $xy = yx$ holds.
    Let $\mathcal{T}_n$ be the full transformation monoid on $n \leq 5$ points.
    Show that the clique numbers of the commuting graph of $\mathcal{T}_n$ are
    $2 ^ {n - 1}$.

    ??? hint

        You can defined $\mathcal{T}_n$ in [GAP][] using
        [`FullTransformationMonoid`](https://docs.gap-system.org/doc/ref/chap53_mj.html#X7D2B0685815B4053),
        and you can compute the clique number
        of digraph using
        [`CliqueNumber`](https://docs.gap-system.org/pkg/digraphs/doc/chap8_mj.html#X78427A8B81FEB457)
        function from the
        [`Digraphs` package for GAP](https://docs.gap-system.org/pkg/digraphs/doc/chap0_mj.html).
        The [`Digraphs` package for GAP](https://docs.gap-system.org/pkg/digraphs/doc/chap0_mj.html)
        is required by the 
        [`Semigroups` package for GAP](https://semigroups.github.io/Semigroups/doc/chap0_mj.html)
        so you don't have to install
        anything new to do this.

3.  Let $S$ be the monoid defined by the presentation
    $\langle a, b, c, d, e, f, g \mid abcd = a^3ea^2, ef= dg\rangle$.

    1.  Show that $S$ is infinite.

    2.  Create a homomorphism from the free semigroup $\{a, b, c, d,
                e, f, g\}^+$ to $S$.

    3.  Partition the first $1000$ elements of the free semigroup
        $\{a, b, c, d, e, f, g\}^+$ so that words belong to the same
        part if and only if they represent the same element of $S$.

    ??? hint
      
        You might find the following helpful:

        * [`SemigroupHomomorphismByImages`](https://semigroups.github.io/Semigroups/doc/chap14_mj.html#X817596438369885B)
        * [`Enumerator`](https://docs.gap-system.org/doc/ref/chap30_mj.html#X7EF8910F82B45EC7)

4.  Is the monoid defined by the presentation
    $$
    \langle x_2, \ldots, x_n\mid x_i^2 = (x_ix_j) ^3 =
          (x_ix_jx_k)^4 = 1\quad i, j, k \text{ distinct}\rangle
    $$ 
    the symmetric group for $n\geq 2$?

    ??? hint

        You might want to use
        [`NumberOfRightCongruences`](https://semigroups.github.io/Semigroups/doc/chap13_mj.html#X7AE16F237E862934).

5.  Determine which of the relations in the presentation are redundant
    and which are not: 
    $$
          \langle a, b \mid 
          a^4=1, b^2= b,
          ba^3ba= a^2(ab)^2, (ba^2)^2= (a^2b)^2, (ba)^2a^2= aba^3b,
          a(ab)^4= (ab)^4 \rangle.
    $$
    What is the minimal set of the relations in this presentation that define
    the same monoid?

6.  Let $S$ be the Catalan monoid of degree $3$.

    1.  Draw the egg-box diagram of $S$.

    2.  Draw the left and right Cayley graphs of $S$.

    3.  Show that $S$ has two non-trivial non-universal non-Rees
        congruences.

    4.  Show that the lattice of left and right congruences of $S$ are
        isomorphic.

    5.  What are the maximal subsemigroups of $S$? Show that none of the
        maximal subsemigroup is isomorphic to any of the others.

    ??? hint

        You might want to look at:

        * [`DotDigraph`](https://docs.gap-system.org/pkg/digraphs/doc/chap9_mj.html#X7F9B99C478EE093A)
        * [`DotString`](https://semigroups.github.io/Semigroups/doc/chap16_mj.html#X853B81B385E2CF36)
        * [`LeftCayleyDigraph`](https://semigroups.github.io/Semigroups/doc/chap11_mj.html#X7EA002E27B10CCE0) and
          [`RightCayleyDigraph`](https://semigroups.github.io/Semigroups/doc/chap11_mj.html#X7EA002E27B10CCE0)
        * [`CongruencesOfSemigroup`](https://semigroups.github.io/Semigroups/doc/chap13_mj.html#X7E8D5BA27CB5A4DA)
        * [`MaximalSubsemigroups`](https://semigroups.github.io/Semigroups/doc/chap11_mj.html#X860A10E387C19150)

7.  Let $S$ be the dual of the full transformation monoid on 5 points.
    Find a transformation representation of $S$ on $32$ points.

    ??? hint

        You might want to look at:

        * [`DualSemigroup`](https://semigroups.github.io/Semigroups/doc/chap8_mj.html#X79F2643C8642A3B0)
        * [`SmallerDegreeTransformationRepresentation`](https://semigroups.github.io/Semigroups/doc/chap14_mj.html#X794E5DA4872989E4)

8.  The translational hull $\Omega(S)$ of a semigroup $S$ is the set of
    all bitranslations $(\lambda, \rho)$ under componentwise
    composition. Any element $s$ of $S$ induces an inner bitranslation
    $(\lambda_s, \rho_s)$ of $S$, where $\lambda_s(x) = sx$ and
    $\rho_s(x) = xs$ for all $x \in S$. This gives a homomorphism
    $\pi_S$ from $S$ to $\Omega(S)$. If this is injective, then $S$ is
    *weakly reductive*. Restricting the bitranslations to an ideal $I$
    of $S$ gives a homomorphism $\pi_{S|I}$ from $S$ to $\Omega(I)$. If
    $I$ is weakly reductive, then $I$ is densely embedded in $S$ if and
    only if $\pi_{S|I}$ is an isomorphism.

    1.  Determine the size of $\Omega(I)$ for each ideal $I$ of $J_7$
        (the Jones monoid of degree 7).

    2.  Which of the ideals of $J_7$ are weakly reductive?

    3.  Which of the ideals of $J_7$ are densely embedded in $J_7$?

    4.  One such $\Omega(I)$ is gigantic, and so is certainly not being
        enumerated. Using\
        `KnownTruePropertiesOfObject`, conjecture how the size is being
        calculated.

    ??? hint

        You might want to look at: 
        [Chapter 18](https://semigroups.github.io/Semigroups/doc/chap18_mj.html)
        of the `Semigroups` package manual.

[GAP]: https://www.gap-system.org/ 
[Semigroups package for GAP]: https://semigroups.github.io/Semigroups/
