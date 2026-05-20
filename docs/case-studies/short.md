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
transformation from the [paper
above](https://doi.org/10.48550/arXiv.2406.19294) for the small values of $n$
not covered by the main theorems in the paper. 

## The symmetric inverse monoid

### $n = 2$
```
sym2 = [[0, 0], []]
s = [
    [1, 1], [1],
    [0, 1, 0, 1, 0, 1, 0], [1, 0, 1],
    ]

I2 = sym2 + s

p = Presentation([0, 1, 2])
p.rules = I2
presentation.replace_word(p, [], [2])
presentation.add_identity_rules(p, 2)

C = Congruence(congruence_kind.twosided)
C.set_number_of_generators(3)
for i in range(0, len(p.rules), 2):
    C.add_pair(p.rules[i], p.rules[i + 1])

C.number_of_classes()
```

### $n = 3$
```
sym3 = [[0, 0], [],
        [1, 1,], [],
        [0, 1, 0], [1, 0, 1]]

s = [
    [2, 2], [2],
    [0, 1, 0, 2], [2, 0, 1, 0],
    [0, 2, 0, 2, 0, 2, 0], [2, 0, 2],
    ]

I3 = sym3 + s

p = Presentation([0, 1, 2, 3])
p.rules = I3
presentation.replace_word(p, [], [3])
presentation.add_identity_rules(p, 3)

C = Congruence(congruence_kind.twosided)
C.set_number_of_generators(4)
for i in range(0, len(p.rules), 2):
    C.add_pair(p.rules[i], p.rules[i + 1])

C.number_of_classes()
```

## The full transformation monoid

### $n = 3$
```
from libsemigroups_pybind11 import presentation, Presentation, congruence_kind, Congruence
from libsemigroups_pybind11.fpsemigroup import author, symmetric_group
sym3 = [[0, 0], [],
        [1, 1], [],
        [0, 1, 0], [1, 0, 1]]

s = [
    [0, 2], [2],
    [2, 1, 2, 1], [2],
    [0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0], [2, 0, 1, 0, 2]
    ]

T3 = sym3 + s

p = Presentation([0, 1, 2, 3])
p.rules = T3
presentation.replace_word(p, [], [3])
presentation.add_identity_rules(p, 3)

C = Congruence(congruence_kind.twosided)
C.set_number_of_generators(4)
for i in range(0, len(p.rules), 2):
    C.add_pair(p.rules[i], p.rules[i + 1])

C.number_of_classes()
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
paper]() this presentation has the smallest number of non-$S_n$
relations, i.e. relations containing the letter $\zeta$ which represents the
rank $n-1$ idempotent:
\begin{pmatrix}
1 & 2 & 3 & 4 \\\\
1 & 1 & 3 & 4
\end{pmatrix}

Note that the presentation with generators $a_2, a_3, a_4$ and the relations in
the presentation in \eqref{eq-t-4} not containing $z$ defines the symmetric
group of degree $4$ (this is Carmichael's presentation from TODO). 

In the [GAP][] code below we show that the presentation defines a
monoid of the same size as $\mathcal{T}_4$ and that the function mapping
$a_2, a_3, a_4, z$ to the permutations $(1, 2), (1, 3), (1, 4)$ and the
transformation $\zeta$ is indeed an isomorphism.

=== "GAP REPL"
    ```gap-repl

      gap> F := FreeMonoid(4);
      <free monoid on the generators [ m1, m2, m3, m4 ]>
      gap> a2 := F.1; a3 := F.2; a4 := F.3; z := F.4;
      m1
      m2
      m3
      m4
      gap> R :=  [[a2^2, One(F)],
      >           [a3^2, One(F)],
      >           [a4^2, One(F)],
      >           [(a2*a3)^3, One(F)],
      >           [(a3*a4)^3, One(F)],
      >           [(a4*a2)^3, One(F)],
      >           [(a2*a3*a2*a4)^2, One(F)],
      >           [(a3*a4*a3*a2)^2, One(F)],
      >           [(a4*a2*a4*a3)^2, One(F)],
      >           [(a4*a2*a3*a2*z)^2,(z*a4*a2*a3*a2)^2],
      >           [(a2*a3*a2*z)^3*a2*a3*a2,z*a2*a3*a2*z],
      >           [a3*a4*a3*z*a3*a4*a3, z*a3*z*a3], [a2*z, z*z*a3*z*a3]];
      [ [ m1^2, <identity ...> ], [ m2^2, <identity ...> ], [ m3^2, <identity ...> ],
      [ (m1*m2)^3, <identity ...> ], [ (m2*m3)^3, <identity ...> ],
      [ (m3*m1)^3, <identity ...> ], [ (m1*m2*m1*m3)^2, <identity ...> ],
      [ (m2*m3*m2*m1)^2, <identity ...> ], [ (m3*m1*m3*m2)^2, <identity ...> ],
      [ (m3*m1*m2*m1*m4)^2, (m4*m3*m1*m2*m1)^2 ],
      [ (m1*m2*m1*m4)^3*m1*m2*m1, m4*m1*m2*m1*m4 ], [ m2*m3*m2*m4*m2*m3*m2, (m4*m2)^2 ],
      [ m1*m4, m4*(m4*m2)^2 ] ]
      gap> M := F / R;
      <fp monoid with 4 generators and 13 relations of length 110>
      gap> Size(M);
      256
      gap> SemigroupIsomorphismByImages(M,
      > FullTransformationMonoid(4),
      > GeneratorsOfMonoid(M),
      > [AsTransformation((1, 2)),
      >  AsTransformation((1, 3)),
      >  AsTransformation((1, 4)),
      >  Transformation([1, 1, 3, 4])]);
      <fp monoid with 4 generators and 13 relations of length 110> ->
      <full transformation monoid of degree 4>
    ```
=== "GAP script"

    ```gap-repl
    F := FreeMonoid(4);
    a2 := F.1; a3 := F.2; a4 := F.3; z := F.4;
    R := [[a2^2, One(F)],
          [a3^2, One(F)],
          [a4^2, One(F)],
          [(a2*a3)^3, One(F)],
          [(a3*a4)^3, One(F)],
          [(a4*a2)^3, One(F)],
          [(a2*a3*a2*a4)^2, One(F)],
          [(a3*a4*a3*a2)^2, One(F)],
          [(a4*a2*a4*a3)^2, One(F)],
          [(a4*a2*a3*a2*z)^2,(z*a4*a2*a3*a2)^2],
          [(a2*a3*a2*z)^3*a2*a3*a2,z*a2*a3*a2*z],
          [a3*a4*a3*z*a3*a4*a3, z*a3*z*a3], [a2*z, z*z*a3*z*a3]];
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

=== "Python REPL"

=== "Python script"

    ```python
    from libsemigroups_pybind11.presentation import examples
    from libsemigroups_pybind11.words import parse_relations as parse
    p = examples.symmetric_group_Car56(4)
    p = to(p, rtype=(Presentation, str))
    p.alphabet("abcz")
    p.rules = p.rules + [parse("(cabaz)^2"), parse("(zcaba)^2"),
           parse("(abaz)^3aba"), "zabaz",
           "bcbzbcb", "zbzb", "az", "zzbzb"]
    tc = ToddCoxeter(congruence_kind.twosided, p)
    tc.number_of_classes() # returns 256
    ```

## Partial transformation monoid

### $n = 2$
The below is some Python to verify that the presentation

\begin{equation}\label{PT-2}
  \left\langlea_2, \ve, \vep}{a_2^2 = 1,\quad  a_2\ve = \ve,\quad  \ve a_2 \vep a_2
  = \ve,\quad  \vep a_2 \ve a_2 = \vep,\quad a_2 \vep a_2 \vep a_2 = \ve \vep\right\rangle
\end{equation}

defines $PT_2$.
1 is epsilon_{1, 2} i.e. ZETA
2 is epsilon_{(1)} i.e. ETA


```
sym2 = [[0, 0], []]

s = [
    [1, 0, 2, 0], [1],
    [2, 0, 1, 0], [2],
    [0, 2, 0, 2, 0], [1, 2],
    [0, 1], [1],
    ]

PT2 = sym2 + s

p = Presentation([0, 1, 2, 3])
p.rules = PT2
presentation.replace_word(p, [], [3])
presentation.add_identity_rules(p, 3)

C = Congruence(congruence_kind.twosided)
C.set_number_of_generators(4)
for i in range(0, len(p.rules), 2):
    C.add_pair(p.rules[i], p.rules[i + 1])

C.number_of_classes()
```

### $n = 3$

```
sym3 = [[0, 0], [],
        [1, 1,], [],
        [0, 1, 0], [1, 0, 1]]

2 is epsilon_{1, 2}
3 is epsilon_{(1)}

s = [
    [2, 0, 3, 0], [2],
    [3, 0, 2, 0], [3],
    [0, 2], [2],
    [0, 1, 0, 3], [3, 0, 1, 0],
    [0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0], [2, 0, 1, 0, 2], # Tn rank n - 2
    [0, 3, 0, 3, 0, 3, 0], [2, 3], # In rank n - 2
    [2, 1, 3, 1], [1, 3, 1, 2] # mixed rank n - 2
    ]

PT3 = sym3 + s

p = Presentation([0, 1, 2, 3, 4])
p.rules = PT3
presentation.replace_word(p, [], [4])
presentation.add_identity_rules(p, 4)

C = Congruence(congruence_kind.twosided)
C.set_number_of_generators(5)
for i in range(0, len(p.rules), 2):
    C.add_pair(p.rules[i], p.rules[i + 1])

C.number_of_classes()
```


### $n = 4$

```
s = [
    [3, 0, 4, 0], [0, 3],
    [4, 0, 3, 0], [0, 1, 0, 4, 0, 1, 0],
    
    [0, 1, 2, 1, 3], [3, 1, 2, 1],
    
    [0, 1, 2, 0, 4], [4, 0, 1, 2, 0],
    
    [0, 1, 0, 3, 0, 1, 0, 3, 0, 1, 0, 3, 0, 1, 0], [3, 0, 1, 0, 3], # Tn rank n - 2
    [3, 0, 1, 0, 2, 3, 0, 1, 0, 2], [0, 1, 0, 2, 3, 0, 1, 0, 2, 3],
    [0, 4, 0, 4, 0], [3, 4], # In rank n - 2
    [3, 1, 4, 1], [1, 4, 1, 3] # mixed rank n - 2
    ]

sym4 = []
for pair in symmetric_group(4):
    sym4.append(pair[0])
    sym4.append(pair[1])


PT4 = sym4 + s

p = Presentation([0, 1, 2, 3, 4, 5])
p.rules = PT4
presentation.replace_word(p, [], [5])
presentation.add_identity_rules(p, 5)

C = Congruence(congruence_kind.twosided)
C.set_number_of_generators(6)
for i in range(0, len(p.rules), 2):
    C.add_pair(p.rules[i], p.rules[i + 1])

C.number_of_classes()
```


[GAP]: https://gap-system.org
[Semigroups package for GAP]: https://semigroups.github.io/Semigroups/
[Python]: https://www.python.org
