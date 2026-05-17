# Worksheet


This worksheet contains some exercises to be completed in `GAP` with the
use of the `Semigroups` package as part of the GAP workshop session of
NBSAN 40. 

1.  Let $J_n$ denote the Jones monoid of degree $n$, and
    $$\input{tikz/jones-element.tikz}$$ be a bipartition of degree 14.

    1.  Find a collection of bipartitions $\{x_1, x_2, \dots,
                x_j\}$ such that the tensor product
        $x_1 \otimes x_2 \otimes
                \dots \otimes x_j$ is equal to $x$. What is the largest
        possible value of $j$? For the definition of the tensor product,
        see the documentation of the function `TensorBipartition`.

    2.  How many elements does $J_{14}$ contain?

    3.  How many idempotent elements does $J_{14}$ contain?

    4.  How many idempotent elements does the Green's
        $\mathscr{D}$-class of $x$ in $J_{14}$ contain?

    5.  How many idempotent elements $e$, for which $7$ is in the domain
        of $e$, does the Green's $\mathscr{D}$-class of $x$ in $J_{14}$
        contain?

    6.  How many irreducible idempotent elements $\hat{e}$, for which
        $7$ is in the domain of $\hat{e}$, does the Green's
        $\mathscr{D}$-class of $x$ in $J_{14}$ contain?

2.  Recall that the commuting graph of a semigroup $S$ is the graph with
    nodes the elements of $S$ and an edge $(x, y)$ if $xy = yx$ holds.
    Let $T_n$ be the full transformation monoid on $n \leq 5$ points.
    Show that the clique numbers of the commuting graph of $T_n$ are
    $2 ^ {n - 1}$.

3.  Let $S$ be the monoid defined by the presentation
    $$\langle a, b, c, d, e, f, g \mid abcd = a^3ea^2, ef= dg\rangle.$$

    1.  Show that $S$ is infinite.

    2.  Create a homomorphism from the free semigroup $\{a, b, c, d,
                e, f, g\}^+$ to $S$.

    3.  Partition the first $1000$ elements of
        $\{a, b, c, d, e, f, g\}^+$ so that words belong to the same
        part if and only if they represent the same element of $S$.

4.  Is the monoid defined by the presentation
    $$\langle x_2, \ldots, x_n\mid x_i^2 = (x_ix_j) ^3 =
          (x_ix_jx_k)^4 = 1\quad i, j, k \text{ distinct}\rangle$$ the
    symmetric group for $n\geq 2$?

5.  Determine which of the relations in the presentation are redundant
    and which are not: $$\begin{align*}
          \langle a, b \mid &\
          a^4=1,  b^2= b,
          ba^3ba= a^2(ab)^2,  (ba^2)^2= (a^2b)^2 ,  (ba)^2a^2= aba^3b,
          a(ab)^4= (ab)^4
          \rangle.
    \end{align*}$$ What is the minimal set of the relations in this
    presentation that define the same monoid?

6.  Let $S$ be the Catalan monoid of degree $3$.

    1.  Draw the egg-box diagram of $S$.

    2.  Draw the left and right Cayley graphs of $S$.

    3.  Show that $S$ has two non-trivial non-universal non-Rees
        congruences.

    4.  Show that the lattice of left and right congruences of $S$ are
        isomorphic.

    5.  What are the maximal subsemigroups of $S$? Show that none of the
        maximal subsemigroup is isomorphic to any of the others.

7.  Let $S$ be the dual of the full transformation monoid on 5 points.
    Find a transformation representation of $S$ on $32$ points.

    1.  Draw the egg-box diagram of $S$.

    2.  Draw the left and right Cayley graphs of $S$.

    3.  Show that $S$ has two non-trivial non-universal non-Rees
        congruences.

    4.  Show that the lattice of left and right congruences of $S$ are
        isomorphic.

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
