# Short presentations for transformation monoids

On this page we describe the computational claims made in the paper:

* T. Aird, J. D. Mitchell, M. T. Whyte, Short presentations for
transformation monoids,
[https://doi.org/10.48550/arXiv.2406.19294](https://doi.org/10.48550/arXiv.2406.19294)

and how they can be verified using
[libsemigroups_pybind11][] and the [Semigroups package for GAP][].

[libsemigroups_pybind11]: https://libsemigroups.github.io/libsemigroups_pybind11/index.html

Below we give the commands that permit the computation of the presentations for
the symmetric inverse monoid, full transformation monoid, and partial
transformation monoid from the [paper
above](https://doi.org/10.48550/arXiv.2406.19294) for the small values of $n$
not covered by the main theorems in the paper. 

## The symmetric inverse monoid

First we include [Python][] code that implements the presentation for the
symmetric inverse monoid of degree $n\geq 3$ from Theorem
1.4 of [the paper](https://doi.org/10.48550/arXiv.2406.19294).


=== "Python"

    ```python
    from libsemigroups_pybind11 import Presentation, presentation, to
    from libsemigroups_pybind11.presentation import examples

    def theorem_1_4_symm_inv(n: int) -> Presentation:
      if n < 3:
        raise TypeError(f"expected <n> to be at least 3, found {n}")
      p = to(examples.symmetric_group_Car56(n), rtype=(Presentation, str))
      alpha = p.alphabet()[-1] + p.alphabet()
      p.alphabet(p.alphabet() + "z")
      
      presentation.add_rule(p, "abaz", "zaba")
      presentation.add_rule(p, alpha + "z", "zz" + alpha)
      presentation.add_rule(p, "azazaza", "zaz")
      return p
    ```

The output of `theorem_1_4_symm_inv` can be converted to [GAP][] input by doing

```python
presentation.to_gap_string(theorem_1_4_symm_inv(3))
```

### $n = 2$

=== "Python"

    ```python
    from libsemigroups_pybind11 import Presentation, congruence_kind, ToddCoxeter
    p = Presentation("az").contains_empty_word(True)
    p.rules = ["a" * 2, "", "z" * 2, "z", "az" * 3 + "a", "zaz"]
    tc = ToddCoxeter(congruence_kind.twosided, p)
    tc.number_of_classes() # returns 7
    ```

=== "GAP"

    ```gap
    F := FreeMonoid("a", "z");
    AssignGeneratorVariables(F);;
    R := [
           [a * a, One(F)],
           [z * z, z],
           [(a * z) ^ 3 * a, z * a * z]
         ];
    S := F / R;
    Size(S); # returns 7
    ```

### $n = 3$

=== "Python"

    ```python
    from libsemigroups_pybind11 import congruence_kind, ToddCoxeter
    p = theorem_1_4_symm_inv(3)
    tc = ToddCoxeter(congruence_kind.twosided, p)
    tc.number_of_classes()  # returns 34
    ```

=== "GAP"

    ```gap
    F := FreeMonoid("a", "b", "z");
    AssignGeneratorVariables(F);;
    R := [
          [a * a, One(F)],
          [b * b, One(F)],
          [a * b * a * b * a * b, One(F)],
          [b * a * b * a * b * a, One(F)],
          [a * b * a * z, z * a * b * a],
          [b * a * b * z, z * z * b * a * b],
          [a * z * a * z * a * z * a, z * a * z]
         ];
    S := F / R;
    Size(S);
    ```

## The full transformation monoid

### $n = 2$

=== "Python"

    ```python
    from libsemigroups_pybind11 import Presentation, congruence_kind, ToddCoxeter

    p = Presentation("az").contains_empty_word(True)
    p.rules = ["aa", "", "az", "z", "zz", "z"]
    tc = ToddCoxeter(congruence_kind.twosided, p)
    tc.number_of_classes()  # returns 4
    ```

=== "GAP"

    ```gap
    F := FreeMonoid("a", "z");
    AssignGeneratorVariables(F);;
    R := [
              [a * a, One(F)],
              [a * z, z],
              [z * z, z]
            ];
    S := F / R;
    Size(S);  # returns 4
    ```

### $n = 3$

=== "Python"

    ```python
    from libsemigroups_pybind11 import Presentation, congruence_kind, ToddCoxeter

    p = Presentation("abz").contains_empty_word(True)
    p.rules = [
        "aa",
        "",
        "bb",
        "",
        "aba",
        "bab",
        "az",
        "z",
        "zb" * 2,
        "z",
        "abaz" * 3 + "aba",
        "zabaz",
    ]
    tc = ToddCoxeter(congruence_kind.twosided, p)
    tc.number_of_classes()  # returns 27
    ```

=== "GAP"

    ```gap
    F := FreeMonoid("a", "b", "z");
    AssignGeneratorVariables(F);;
    R := [
           [a * a, One(F)],
           [b * b, One(F)],
           [a * b * a, b * a * b],
           [a * z, z],
           [z * b * z * b, z],
           [(a * b * a * z) ^ 3 * a * b * a, z * a * b * a * z]
         ];
    S := F / R;
    Size(S);  # returns 27
    ```

### $n = 4$

Here we give the [GAP][] and [Python][] code for verifying that the
presentation
\begin{equation}\label{eq-t-4}
\begin{aligned}
\langle a_2, a_3, a_4, z \mid &\ 
      a_2^2=\varepsilon,
      a_3^2=\varepsilon,
      a_4^2=\varepsilon,
      (a_2a_3)^3=\varepsilon,
      (a_3a_4)^3=\varepsilon,
      (a_4a_2)^3=\varepsilon,\\\\
      &\ (a_2a_3a_2a_4)^2=\varepsilon,
      (a_3a_4a_3a_2)^2=\varepsilon,
      (a_4a_2a_4a_3)^2=\varepsilon, \\\\
&\ (a_4a_2a_3a_2z)^2=(za_4a_2a_3a_2)^2, \\\\
&\      (a_2a_3a_2z)^3a_2a_3a_2=za_2a_3a_2z,\\\\
&\      a_3a_4a_3za_3a_4a_3=(za_3)^2, \\\\
&\ a_2z= z(za_3)^2
\rangle
\end{aligned}
\end{equation}
defines the full transformation monoid of degree $4$. By Theorem 1.5 in [the
paper](https://doi.org/10.48550/arXiv.2406.19294) this presentation has the smallest number of non-$S_n$
relations, i.e. relations containing the letter $\zeta$ which represents the
rank $n-1$ idempotent:
\begin{pmatrix}
1 & 2 & 3 & 4 \\\\
1 & 1 & 3 & 4
\end{pmatrix}

Note that the presentation with generators $a_2, a_3, a_4$ and the relations in
the presentation in \eqref{eq-t-4} not containing $z$ defines the symmetric
group of degree $4$ (this is Carmichael's presentation from:

* Carmichael, Robert D. *Introduction to the Theory of Groups of Finite Order*.
  New York: Dover Publications, 1956). 

In the [GAP][] code below we show that the presentation defines a
monoid of the same size as $\mathcal{T}_4$ and that the function mapping
$a_2, a_3, a_4, z$ to the permutations $(1, 2), (1, 3), (1, 4)$ and the
transformation $\zeta$ is indeed an isomorphism.

=== "Python"

    ```python
    from libsemigroups_pybind11 import Presentation, ToddCoxeter, congruence_kind, to
    from libsemigroups_pybind11.presentation import examples
    from libsemigroups_pybind11.words import parse_relations as parse
    p = examples.symmetric_group_Car56(4)
    p = to(p, rtype=(Presentation, str))
    p.alphabet("abcz")
    p.rules = p.rules + [
        parse("(cabaz)^2"),
        parse("(zcaba)^2"),
        parse("(abaz)^3aba"),
        "zabaz",
        "bcbzbcb",
        "zbzb",
        "az",
        "zzbzb",
    ]
    tc = ToddCoxeter(congruence_kind.twosided, p)
    tc.number_of_classes()  # returns 256
    ```

=== "GAP"

    ```gap
    F := FreeMonoid("a", "b", "c", "z");
    AssignGeneratorVariables(F);;
    R := [[a^2, One(F)],
          [b^2, One(F)],
          [c^2, One(F)],
          [(a*b)^3, One(F)],
          [(b*c)^3, One(F)],
          [(c*a)^3, One(F)],
          [(a*b*a*c)^2, One(F)],
          [(b*c*b*a)^2, One(F)],
          [(c*a*c*b)^2, One(F)],
          [(c*a*b*a*z)^2,(z*c*a*b*a)^2],
          [(a*b*a*z)^3*a*b*a,z*a*b*a*z],
          [b*c*b*z*b*c*b, z*b*z*b], [a*z, z*z*b*z*b]];
    M := F / R;
    Size(M);
    SemigroupIsomorphismByImages(M, 
     FullTransformationMonoid(4), 
     GeneratorsOfMonoid(M),
     [AsTransformation((1, 2)), 
      AsTransformation((1, 3)), 
      AsTransformation((1, 4)),
      Transformation([1, 1, 3, 4])]);
    ```

### $n = 5$

As stated in [the paper](https://doi.org/10.48550/arXiv.2406.19294), the presentation from Theorem 1.5 defines $T_n$
when $n = 5$. 

```python
from libsemigroups_pybind11 import Presentation, presentation, to
from libsemigroups_pybind11.presentation import examples

def theorem_1_5_full_transf(n: int) -> Presentation:
    if n != 5 and n < 7:
        raise TypeError(f"expected <n> to be at least 5 or at least 7, found {n}")
    p = to(examples.symmetric_group_Car56(n), rtype=(Presentation, str))
    A = p.alphabet()

    if n % 2 == 1:
        alpha = A[1] + A[2] + A[1]
        beta = A[1:] + A[1]
    else:
        alpha = A[1:] + A[1]
        beta = A[1] + A[5] + A[4] + A[2] + A[3] + A[1]

    inv_alpha = "".join(reversed(alpha))
    inv_beta = "".join(reversed(beta))

    p.alphabet(A + "z")
    z = "z"

    presentation.add_rule(
        p,
        A[-1] + A[0] + A[1] + A[0] + z + A[-1] + A[0] + A[1] + A[0] + z,
        z + A[-1] + A[0] + A[1] + A[0] + z + A[-1] + A[0] + A[1] + A[0],
    )
    presentation.add_rule(
        p, (A[0] + A[1] + A[0] + z) * 3 + A[0] + A[1] + A[0], z + A[0] + A[1] + A[0] + z
    )
    presentation.add_rule(p, inv_alpha + z + alpha, (z + A[1]) * 2)
    presentation.add_rule(p, inv_beta + z + beta, A[0] + (z + A[1]) * 2)

    return p
```

=== "Python"

    ```python
    from libsemigroups_pybind11 import ToddCoxeter, congruence_kind
    p = theorem_1_5_full_transf(5)
    tc = ToddCoxeter(congruence_kind.twosided, p)
    tc.number_of_classes()  # returns 3125
    ```

=== "GAP"

    ```gap
    F := FreeMonoid("a", "b", "c", "d", "z");
    AssignGeneratorVariables(F);;
    R := [
          [a * a, One(F)],
          [b * b, One(F)],
          [c * c, One(F)],
          [d * d, One(F)],
          [a * b * a * b * a * b, One(F)],
          [b * c * b * c * b * c, One(F)],
          [c * d * c * d * c * d, One(F)],
          [d * a * d * a * d * a, One(F)],
          [a * b * a * c * a * b * a * c, One(F)],
          [a * b * a * d * a * b * a * d, One(F)],
          [b * c * b * a * b * c * b * a, One(F)],
          [b * c * b * d * b * c * b * d, One(F)],
          [c * d * c * a * c * d * c * a, One(F)],
          [c * d * c * b * c * d * c * b, One(F)],
          [d * a * d * b * d * a * d * b, One(F)],
          [d * a * d * c * d * a * d * c, One(F)],
          [d * a * b * a * z * d * a * b * a * z, z * d * a * b * a * z * d * a * b * a],
          [a * b * a * z * a * b * a * z * a * b * a * z * a * b * a, z * a * b * a * z],
          [b * c * b * z * b * c * b, z * b * z * b],
          [b * d * c * b * z * b * c * d * b, a * z * b * z * b]
        ];
    S := F / R;
    ```

### $n = 6$

=== "Python"

    ```python
    from libsemigroups_pybind11 import (
        Presentation,
        presentation,
        congruence_kind,
        ToddCoxeter, 
        to
    )
    from libsemigroups_pybind11.presentation import examples
    from datetime import timedelta

    p = examples.symmetric_group_Car56(6)
    p = to(p, rtype=(Presentation, str))
    A = p.alphabet()
    z = "z"
    p.alphabet(A + z)

    presentation.add_rule(
        p, (z + A[4] + A[0] + A[1] + A[0]) * 2, (A[4] + A[0] + A[1] + A[0] + z) * 2
    )
    presentation.add_rule(
        p, (A[0] + A[1] + A[0] + z) * 3 + A[0] + A[1] + A[0], z + A[0] + A[1] + A[0] + z
    )
    presentation.add_rule(
        p, A[1] + A[2] + A[1] + z + A[1] + A[2] + A[1], z + A[1] + z + A[1]
    )
    presentation.add_rule(
        p, A[1] + A[4] + A[3] + A[2] + A[1] + z + A[1] + A[2] + A[3] + A[4] + A[1], A[0] + z
    )

    tc = ToddCoxeter(congruence_kind.twosided, p)
    tc.run_for(timedelta(seconds=10))
    tc.perform_lookahead()
    tc.perform_lookahead()
    tc.perform_lookahead()
    tc.number_of_classes()  # returns 46656
    ```

=== "GAP"

    ```gap
    F := FreeMonoid("a", "b", "c", "d", "e", "f");
    AssignGeneratorVariables(F);;
    R := [
          [a * a, One(F)],
          [b * b, One(F)],
          [c * c, One(F)],
          [d * d, One(F)],
          [e * e, One(F)],
          [a * b * a * b * a * b, One(F)],
          [b * c * b * c * b * c, One(F)],
          [c * d * c * d * c * d, One(F)],
          [d * e * d * e * d * e, One(F)],
          [e * a * e * a * e * a, One(F)],
          [a * b * a * c * a * b * a * c, One(F)],
          [a * b * a * d * a * b * a * d, One(F)],
          [a * b * a * e * a * b * a * e, One(F)],
          [b * c * b * a * b * c * b * a, One(F)],
          [b * c * b * d * b * c * b * d, One(F)],
          [b * c * b * e * b * c * b * e, One(F)],
          [c * d * c * a * c * d * c * a, One(F)],
          [c * d * c * b * c * d * c * b, One(F)],
          [c * d * c * e * c * d * c * e, One(F)],
          [d * e * d * a * d * e * d * a, One(F)],
          [d * e * d * b * d * e * d * b, One(F)],
          [d * e * d * c * d * e * d * c, One(F)],
          [e * a * e * b * e * a * e * b, One(F)],
          [e * a * e * c * e * a * e * c, One(F)],
          [e * a * e * d * e * a * e * d, One(F)],
          [f * e * a * b * a * f * e * a * b * a, e * a * b * a * f * e * a * b * a * f],
          [a * b * a * f * a * b * a * f * a * b * a * f * a * b * a, f * a * b * a * f],
          [b * c * b * f * b * c * b, f * b * f * b],
          [b * e * d * c * b * f * b * c * d * e * b, a * f]
        ];
    S := F / R;
    Size(S);  # returns 46656
    ```

## Partial transformation monoid

### $n = 2$

The below is some [Python][] to verify that the presentation
\begin{equation}\label{PT-2}
  \langle a_2, \zeta, \eta \mid a_2^2 = 1,\quad  a_2\zeta = \zeta,\quad  \zeta a_2 \eta a_2
  = \zeta,\quad  \eta a_2 \zeta a_2 = \eta,\quad a_2 \eta a_2 \eta a_2 = \zeta \eta \rangle
\end{equation}
defines $PT_2$.

=== "Python"

    ```python
    from libsemigroups_pybind11 import (
        Presentation,
        congruence_kind,
        ToddCoxeter,
    )

    p = Presentation("azn").contains_empty_word(True)
    p.rules = ["aa", "", "az", "z", "zana", "z", "naza", "n", "anana", "zn"]
    
    tc = ToddCoxeter(congruence_kind.twosided, p)
    tc.number_of_classes()  # returns 9
    ```

=== "GAP"

    ```gap
    F := FreeMonoid("a", "z", "n");
    AssignGeneratorVariables(F);;
    R := [
           [a * a, One(F)],
           [a * z, z],
           [z * a * n * a, z],
           [n * a * z * a, n],
           [a * n * a * n * a, z * n]
         ];
    S := F / R;
    Size(S);
    ```

### $n = 3$

=== "Python"

    ```python
    from libsemigroups_pybind11 import (
        Presentation,
        congruence_kind,
        ToddCoxeter,
        to
    )
    from libsemigroups_pybind11.presentation import examples

    p = to(examples.symmetric_group_Car56(3), rtype=(Presentation, str))
    p.alphabet("abzn")
    p.rules = p.rules + [
        "zana",
        "z",
        "naza",
        "n",
        "az",
        "z",
        "aban",
        "naba",
        "abazabazaba",
        "zabaz",
        "ananana",
        "zn",
        "zbnb",
        "bnbz",
    ]

    tc = ToddCoxeter(congruence_kind.twosided, p)
    tc.number_of_classes()  # returns 64
    ```

=== "GAP"

    ```gap
    F := FreeMonoid("a", "b", "z", "n");
    AssignGeneratorVariables(F);;
    R := [
           [a * a, One(F)],
           [b * b, One(F)],
           [a * b * a * b * a * b, One(F)],
           [b * a * b * a * b * a, One(F)],
           [z * a * n * a, z],
           [n * a * z * a, n],
           [a * z, z],
           [a * b * a * n, n * a * b * a],
           [a * b * a * z * a * b * a * z * a * b * a, z * a * b * a * z],
           [a * n * a * n * a * n * a, z * n],
           [z * b * n * b, b * n * b * z]
         ];
    S := F / R;
    Size(S);
    ```

### $n = 4$, $5$, and $6$

```python
from libsemigroups_pybind11 import Presentation, ToddCoxeter, to, congruence_kind
from libsemigroups_pybind11.presentation import examples

def partial_transf_monoid_456(n: int) -> Presentation:
  if n not in (4, 5, 6):
    raise TypeError(f"expected <n> to be 4, 5, or 6, found {n}")
  p = to(examples.symmetric_group_Car56(n), rtype=(Presentation, str))
  A = p.alphabet()
  p.alphabet(p.alphabet() + "zn")
  p.rules = p.rules + [
    "n" + A + A[0], A + A[0] + "n",
    A[-1] + A[0] + A[1] + A[0] + "z" + A[-1] + A[0] + A[1] + A[0] + "z",
    "z" + A[-1] + A[0] + A[1] + A[0] + "z" + A[-1] + A[0] + A[1] + A[0],
    (A[0] + A[1] + A[0] + "z") * 3 + A[0] + A[1] + A[0], 
    "z" + A[0] + A[1] + A[0] + "z",
    A[1] + A[2:] + A[1] + A[0] + "z", 
    "z" + A[1] + A[2:] + A[1],
    "zbnb", "bnbz",
    "zn", "anana",
    "abanaba", "naza",
    "bcbzbcb", "zana"
  ]
  return p
```

#### $n = 4$

=== "Python"

    ```python
    p = partial_transf_monoid_456(4)
    tc = ToddCoxeter(congruence_kind.twosided, p)
    tc.number_of_classes()  # returns 625
    ```

=== "GAP"

    ```gap
    F := FreeMonoid("a", "b", "c", "z", "n");
    AssignGeneratorVariables(F);;
    R := [
           [a * a, One(F)],
           [b * b, One(F)],
           [c * c, One(F)],
           [a * b * a * b * a * b, One(F)],
           [b * c * b * c * b * c, One(F)],
           [c * a * c * a * c * a, One(F)],
           [a * b * a * c * a * b * a * c, One(F)],
           [b * c * b * a * b * c * b * a, One(F)],
           [c * a * c * b * c * a * c * b, One(F)],
           [n * a * b * c * a, a * b * c * a * n],
           [c * a * b * a * z * c * a * b * a * z, z * c * a * b * a * z * c * a * b * a],
           [a * b * a * z * a * b * a * z * a * b * a * z * a * b * a, z * a * b * a * z],
           [b * c * b * a * z, z * b * c * b],
           [z * b * n * b, b * n * b * z],
           [z * n, a * n * a * n * a],
           [a * b * a * n * a * b * a, n * a * z * a],
           [b * c * b * z * b * c * b, z * a * n * a]
         ];
    S := F / R;
    Size(S);
    ```

#### $n = 5$

=== "Python"

    ```python
    p = partial_transf_monoid_456(5)
    tc = ToddCoxeter(congruence_kind.twosided, p)
    tc.number_of_classes()  # returns 7776
    ```

=== "GAP"

    ```gap
    F := FreeMonoid("a", "b", "c", "d", "z", "n");
    AssignGeneratorVariables(F);;
    R := [
           [a * a, One(F)],
           [b * b, One(F)],
           [c * c, One(F)],
           [d * d, One(F)],
           [a * b * a * b * a * b, One(F)],
           [b * c * b * c * b * c, One(F)],
           [c * d * c * d * c * d, One(F)],
           [d * a * d * a * d * a, One(F)],
           [a * b * a * c * a * b * a * c, One(F)],
           [a * b * a * d * a * b * a * d, One(F)],
           [b * c * b * a * b * c * b * a, One(F)],
           [b * c * b * d * b * c * b * d, One(F)],
           [c * d * c * a * c * d * c * a, One(F)],
           [c * d * c * b * c * d * c * b, One(F)],
           [d * a * d * b * d * a * d * b, One(F)],
           [d * a * d * c * d * a * d * c, One(F)],
           [n * a * b * c * d * a, a * b * c * d * a * n],
           [d * a * b * a * z * d * a * b * a * z, z * d * a * b * a * z * d * a * b * a],
           [a * b * a * z * a * b * a * z * a * b * a * z * a * b * a, z * a * b * a * z],
           [b * c * d * b * a * z, z * b * c * d * b],
           [z * b * n * b, b * n * b * z],
           [z * n, a * n * a * n * a],
           [a * b * a * n * a * b * a, n * a * z * a],
           [b * c * b * z * b * c * b, z * a * n * a]
        ];
    S := F / R;
    Size(S);
    ```

#### $n = 6$

=== "Python"

    ```python
    p = partial_transf_monoid_456(6)
    tc = ToddCoxeter(congruence_kind.twosided, p)
    tc.number_of_classes()  # returns 117649
    ```

=== "GAP"

    ```gap
    F := FreeMonoid("a", "b", "c", "d", "e", "z", "n");
    AssignGeneratorVariables(F);;
    R := [
           [a * a, One(F)],
           [b * b, One(F)],
           [c * c, One(F)],
           [d * d, One(F)],
           [e * e, One(F)],
           [a * b * a * b * a * b, One(F)],
           [b * c * b * c * b * c, One(F)],
           [c * d * c * d * c * d, One(F)],
           [d * e * d * e * d * e, One(F)],
           [e * a * e * a * e * a, One(F)],
           [a * b * a * c * a * b * a * c, One(F)],
           [a * b * a * d * a * b * a * d, One(F)],
           [a * b * a * e * a * b * a * e, One(F)],
           [b * c * b * a * b * c * b * a, One(F)],
           [b * c * b * d * b * c * b * d, One(F)],
           [b * c * b * e * b * c * b * e, One(F)],
           [c * d * c * a * c * d * c * a, One(F)],
           [c * d * c * b * c * d * c * b, One(F)],
           [c * d * c * e * c * d * c * e, One(F)],
           [d * e * d * a * d * e * d * a, One(F)],
           [d * e * d * b * d * e * d * b, One(F)],
           [d * e * d * c * d * e * d * c, One(F)],
           [e * a * e * b * e * a * e * b, One(F)],
           [e * a * e * c * e * a * e * c, One(F)],
           [e * a * e * d * e * a * e * d, One(F)],
           [n * a * b * c * d * e * a, a * b * c * d * e * a * n],
           [e * a * b * a * z * e * a * b * a * z, z * e * a * b * a * z * e * a * b * a],
           [a * b * a * z * a * b * a * z * a * b * a * z * a * b * a, z * a * b * a * z],
           [b * c * d * e * b * a * z, z * b * c * d * e * b],
           [z * b * n * b, b * n * b * z],
           [z * n, a * n * a * n * a],
           [a * b * a * n * a * b * a, n * a * z * a],
           [b * c * b * z * b * c * b, z * a * n * a]
         ];
    S := F / R;
    Size(S);
    ```

[GAP]: https://gap-system.org
[Semigroups package for GAP]: https://semigroups.github.io/Semigroups/
[Python]: https://www.python.org
