# Tits group T

The claims on this page come from
[https://brauer.maths.qmul.ac.uk/Atlas/v3/exc/TF42/](https://brauer.maths.qmul.ac.uk/Atlas/v3/exc/TF42/).

## Claim

$$
    \mathrm{T} = \langle a, b \mid a^2 = b^3 = (ab)^{13} = [a, b]^5 = [a, bab]^4 = ((ab)^4ab^{−1})^6 = 1 \rangle
$$

with

$$
    |\mathrm{T}| = 17,971,200.
$$

On this page, we verify that the above claimed presentation of the Tits group
T~3~ defines a group of order $17,971,200$.

## The code

In [libsemigroups_pybind11][], the following script constructs the presentation
for T and runs the Todd-Coxeter algorithm.

<details markdown>
<summary>Code</summary>

```python
from libsemigroups_pybind11 import (
    Presentation,
    ToddCoxeter,
    congruence_kind,
    presentation,
)
from libsemigroups_pybind11.words import parse_relations

# Setup the presentation object with the empty word and inverses, so it can represent a group
p = Presentation("abAB")
p.contains_empty_word(True)
presentation.add_inverse_rules(p, "ABab")

# Add the defining relations
presentation.add_rule(p, parse_relations("a^2"), "")
presentation.add_rule(p, parse_relations("b^3"), "")
presentation.add_rule(p, parse_relations("(ab)^13"), "")
presentation.add_rule(p, parse_relations("(a,b)^5"), "")
presentation.add_rule(p, parse_relations("(a,bab)^4"), "")
presentation.add_rule(p, parse_relations("(ababababaB)^6"), "")

presentation.balance(p, "abAB", "ABab")
presentation.replace_subword(p, "A", "a")
presentation.replace_subword(p, "B", "bb")
p.alphabet("ab")

tc = ToddCoxeter(congruence_kind.twosided, p)
tc.strategy(ToddCoxeter.options.strategy.felsch)

print(f"The size of the group is {tc.number_of_classes()}")
```

</details>

## The output

The truncated output of the enumeration is below:

??? info "Truncated output from the Python script"

    ```
    ++++++++++++++++++++++++++++++++
    #0: ToddCoxeter: RUN 0 START (strategy() = felsch)
    #0: ToddCoxeter: |A| = 2, |R| = 10, |u| + |v| ∈ [2, 75], ∑(|u| + |v|) = 190
    ++++++++++++++++++++++++++++++++
    #0: ToddCoxeter: FELSCH 0.0 START
    #0: ToddCoxeter: FELSCH 0.0.0     |       active |          killed |        defined
    #0: ToddCoxeter: nodes            |            1 |               0 |              1
    #0: ToddCoxeter:                  |       active |         missing |     % complete
    #0: ToddCoxeter: edges            |            0 |               2 |           0.0%
    #0: ToddCoxeter: time             | run 0 = 28µs | all runs = 28µs | elapsed = 99µs
    ++++++++++++++++++++++++++++++++
    #1: ToddCoxeter: FELSCH 0.0.1       |         active |            killed |          defined
    #1: ToddCoxeter: nodes              |        931,110 |            56,827 |          987,966
    #1: ToddCoxeter: diff 0.0.0         |       +931,109 |           +56,827 |         +987,965
    #1: ToddCoxeter:                    |         active |           missing |       % complete
    #1: ToddCoxeter: edges              |      1,636,776 |           225,444 |            87.9%
    #1: ToddCoxeter: diff 0.0.0         |     +1,636,776 |          +225,442 |           +87.9%
    #1: ToddCoxeter: phase 0.0 = 1.000s | run 0 = 1.000s | all runs = 1.000s | elapsed = 1.000s
    ++++++++++++++++++++++++++++++++
    #1: ToddCoxeter: FELSCH 0.0.2       |         active |            killed |          defined
    #1: ToddCoxeter: nodes              |      1,689,659 |           107,031 |        1,796,700
    #1: ToddCoxeter: diff 0.0.1         |       +758,549 |           +50,204 |         +808,734
    #1: ToddCoxeter: diff 0.0.0         |     +1,689,658 |          +107,031 |       +1,796,699
    #1: ToddCoxeter:                    |         active |           missing |       % complete
    #1: ToddCoxeter: edges              |      2,979,269 |           400,049 |            88.2%
    #1: ToddCoxeter: diff 0.0.1         |     +1,342,493 |          +174,605 |            +0.3%
    #1: ToddCoxeter: diff 0.0.0         |     +2,979,269 |          +400,047 |           +88.2%
    #1: ToddCoxeter: phase 0.0 = 2.000s | run 0 = 2.000s | all runs = 2.000s | elapsed = 2.000s
    ++++++++++++++++++++++++++++++++
    #1: ToddCoxeter: FELSCH 0.0.3       |         active |            killed |          defined
    #1: ToddCoxeter: nodes              |      2,422,503 |           156,074 |        2,578,589
    #1: ToddCoxeter: diff 0.0.2         |       +732,844 |           +49,043 |         +781,889
    #1: ToddCoxeter: diff 0.0.0         |     +2,422,502 |          +156,074 |       +2,578,588
    #1: ToddCoxeter:                    |         active |           missing |       % complete
    #1: ToddCoxeter: edges              |      4,279,477 |           565,529 |            88.3%
    #1: ToddCoxeter: diff 0.0.2         |     +1,300,208 |          +165,480 |            +0.2%
    #1: ToddCoxeter: diff 0.0.0         |     +4,279,477 |          +565,527 |           +88.3%
    #1: ToddCoxeter: phase 0.0 = 3.001s | run 0 = 3.001s | all runs = 3.001s | elapsed = 3.001s
    ++++++++++++++++++++++++++++++++
    #1: ToddCoxeter: FELSCH 0.0.4       |         active |            killed |          defined
    #1: ToddCoxeter: nodes              |      3,109,354 |           202,556 |        3,311,914
    #1: ToddCoxeter: diff 0.0.3         |       +686,851 |           +46,482 |         +733,325
    #1: ToddCoxeter: diff 0.0.0         |     +3,109,353 |          +202,556 |       +3,311,913
    #1: ToddCoxeter:                    |         active |           missing |       % complete
    #1: ToddCoxeter: edges              |      5,499,715 |           718,993 |            88.4%
    #1: ToddCoxeter: diff 0.0.3         |     +1,220,238 |          +153,464 |            +0.1%
    #1: ToddCoxeter: diff 0.0.0         |     +5,499,715 |          +718,991 |           +88.4%
    #1: ToddCoxeter: phase 0.0 = 4.001s | run 0 = 4.001s | all runs = 4.001s | elapsed = 4.001s
    ++++++++++++++++++++++++++++++++
    [... lines omitted ...]
    ++++++++++++++++++++++++++++++++
    #0: ToddCoxeter: FELSCH 0.2.53       |          active |             killed |           defined
    #0: ToddCoxeter: nodes               |      17,971,200 |          3,439,895 |        21,411,095
    #0: ToddCoxeter: diff 0.2.52         |              +0 |                 +0 |                +0
    #0: ToddCoxeter: diff 0.2.0          |              +0 |                 +0 |                +0
    #0: ToddCoxeter:                     |          active |            missing |        % complete
    #0: ToddCoxeter: edges               |      35,942,400 |                  0 |            100.0%
    #0: ToddCoxeter: diff 0.2.52         |              +0 |                 +0 |             +0.0%
    #0: ToddCoxeter: diff 0.2.0          |              +0 |                 +0 |             +0.0%
    #0: ToddCoxeter: phase 0.2 = 51.384s | run 0 = 3min37s | all runs = 3min37s | elapsed = 3min37s
    ++++++++++++++++++++++++++++++++
    #0: ToddCoxeter: RUN 0 STOP (finished)
    #0: ToddCoxeter: run 0                |       lookahead |         lookbehind |               hlt |        felsch
    #0: ToddCoxeter: num. phases          |               1 |                  0 |                 0 |             1
    #0: ToddCoxeter: time spent in phases |   51.384s (24%) |             - (0%) |            - (0%) | 2min46s (76%)
    #0: ToddCoxeter: phase 0.2 = 51.594s  | run 0 = 3min37s | all runs = 3min37s | elapsed = 3min37s
    The size of the group is 17971200
    ```

:material-checkbox-marked-circle-outline: The computed size of the group matches
the size of the group provided on the ATLAS: $17,971,200$.
