# Rudvalis group Ru

The claims on this page come from
[Bradley, Curtis and Malik (2010)](https://doi.org/10.1112/jlms/jdq039).

## Claim

$$
    \mathrm{Ru} = \langle a, b, c, t \mid a^7 = b^3 = c^2 = t^2 = (cb)^{-1}bc = (ct)^{-1}tc = (ac)^6 = ((ca)^{-1}ac)^4 = (bt)^3 = b^{-1}aba^{-2} = (abc)^7 = (ab^2t)^3 = (bacat)^{-1}acat(aca)^{-1}baca = (bt)^{-1}(ca)^{-2}acabt(acab)^{-1}(ca)^2b = ta^{-3}ta^3b^{-1}ta^{-1}tab(aca)^{-2}(a^{-3}c^{-1})^2a^3ca^5ca \rangle
$$

and

$$
    \mathrm{A}_{8} = \mathrm{Ru} \mathbin{/} \langle a, b, c \rangle
$$

with

$$
    [\mathrm{Ru} : \mathrm{A}_8] = 7,238,400.
$$

On this page, we verify that the above subgroup of the Rudvalis group Ru defines
a group of the correct index.

## The code

In [libsemigroups_pybind11][], the following script constructs the presentation
for M~23~, adds the generating pairs that define the subgroup M~11~, and runs
the Todd-Coxeter algorithm.

```python
from libsemigroups_pybind11 import (
    Presentation,
    ToddCoxeter,
    congruence_kind,
    presentation,
)
from libsemigroups_pybind11.words import parse_relations

p = Presentation("abctABCT").contains_empty_word(True)
presentation.add_inverse_rules(p, "ABCTabct")
presentation.add_rule(p, parse_relations("a^7"), "")
presentation.add_rule(p, parse_relations("b^3"), "")
presentation.add_rule(p, parse_relations("c^2"), "")
presentation.add_rule(p, parse_relations("t^2"), "")
presentation.add_rule(p, parse_relations("BCbc"), "")
presentation.add_rule(p, parse_relations("TCtc"), "")
presentation.add_rule(p, parse_relations("(ac)^6"), "")
presentation.add_rule(p, parse_relations("(ACac)^4"), "")
presentation.add_rule(p, parse_relations("(bt)^3"), "")
presentation.add_rule(p, parse_relations("BabA^2"), "")
presentation.add_rule(p, parse_relations("(abc)^7"), "")
presentation.add_rule(p, parse_relations("(ab^2t)^3"), "")
presentation.add_rule(p, parse_relations("TACABacatACAbaca"), "")
presentation.add_rule(p, parse_relations("TB(AC)^2acabtBACA(ca)^2b"), "")
presentation.add_rule(p, parse_relations("tA^3ta^3BtAtabACA^2(A^3C)^2a^3ca^5ca"), "")
presentation.balance(p, p.alphabet(), "ABCTabct")

tc = ToddCoxeter(congruence_kind.onesided, p)

tc.add_generating_pair("a", "")
tc.add_generating_pair("b", "")
tc.add_generating_pair("c", "")

tc.strategy(ToddCoxeter.options.strategy.felsch).use_relations_in_extra(True)
tc.run()

print(f"The index of the subgroup is {tc.number_of_classes()}")
```

## The output

The truncated output of the enumeration is below:

??? info "Truncated output from the Python script"

    ```
    ++++++++++++++++++++++++++++++++
    #0: ToddCoxeter: RUN 0 START (strategy() = felsch)
    #0: ToddCoxeter: |A| = 8, |R| = 23, |u| + |v| ∈ [2, 37], ∑(|u| + |v|) = 183
    ++++++++++++++++++++++++++++++++
    #0: ToddCoxeter: FELSCH 0.0 START
    #0: ToddCoxeter: FELSCH 0.0.0     |        active |           killed |         defined
    #0: ToddCoxeter: nodes            |            21 |               18 |              39
    #0: ToddCoxeter:                  |        active |          missing |      % complete
    #0: ToddCoxeter: edges            |            68 |              100 |           40.5%
    #0: ToddCoxeter: time             | run 0 = 146µs | all runs = 146µs | elapsed = 236µs
    ++++++++++++++++++++++++++++++++
    #1: ToddCoxeter: FELSCH 0.0.1       |         active |            killed |          defined
    #1: ToddCoxeter: nodes              |        537,051 |           187,750 |          724,832
    #1: ToddCoxeter: diff 0.0.0         |       +537,030 |          +187,732 |         +724,793
    #1: ToddCoxeter:                    |         active |           missing |       % complete
    #1: ToddCoxeter: edges              |      2,308,258 |         1,988,150 |            53.7%
    #1: ToddCoxeter: diff 0.0.0         |     +2,308,190 |        +1,988,050 |           +13.2%
    #1: ToddCoxeter: phase 0.0 = 1.000s | run 0 = 1.000s | all runs = 1.000s | elapsed = 1.000s
    ++++++++++++++++++++++++++++++++
    #1: ToddCoxeter: FELSCH 0.0.2       |         active |            killed |          defined
    #1: ToddCoxeter: nodes              |      1,188,023 |           273,755 |        1,461,793
    #1: ToddCoxeter: diff 0.0.1         |       +650,972 |           +86,005 |         +736,961
    #1: ToddCoxeter: diff 0.0.0         |     +1,188,002 |          +273,737 |       +1,461,754
    #1: ToddCoxeter:                    |         active |           missing |       % complete
    #1: ToddCoxeter: edges              |      5,066,218 |         4,437,966 |            53.3%
    #1: ToddCoxeter: diff 0.0.1         |     +2,757,960 |        +2,449,816 |            -0.4%
    #1: ToddCoxeter: diff 0.0.0         |     +5,066,150 |        +4,437,866 |           +12.8%
    #1: ToddCoxeter: phase 0.0 = 2.000s | run 0 = 2.001s | all runs = 2.001s | elapsed = 2.001s
    ++++++++++++++++++++++++++++++++
    #1: ToddCoxeter: FELSCH 0.0.3       |         active |            killed |          defined
    #1: ToddCoxeter: nodes              |      1,782,973 |           360,686 |        2,143,668
    #1: ToddCoxeter: diff 0.0.2         |       +594,950 |           +86,931 |         +681,875
    #1: ToddCoxeter: diff 0.0.0         |     +1,782,952 |          +360,668 |       +2,143,629
    #1: ToddCoxeter:                    |         active |           missing |       % complete
    #1: ToddCoxeter: edges              |      7,622,880 |         6,640,904 |            53.4%
    #1: ToddCoxeter: diff 0.0.2         |     +2,556,662 |        +2,202,938 |            +0.1%
    #1: ToddCoxeter: diff 0.0.0         |     +7,622,812 |        +6,640,804 |           +13.0%
    #1: ToddCoxeter: phase 0.0 = 3.001s | run 0 = 3.001s | all runs = 3.001s | elapsed = 3.001s
    #0: ToddCoxeter: large collapse, number of coincidences 100,003 >= 100,000 = large_collapse()!
    ++++++++++++++++++++++++++++++++
    [... lines omitted ...]
    ++++++++++++++++++++++++++++++++
    #0: ToddCoxeter: FELSCH 0.2.26       |         active |            killed |          defined
    #0: ToddCoxeter: nodes               |      7,238,400 |        23,613,836 |       30,852,236
    #0: ToddCoxeter: diff 0.2.25         |             +0 |                +0 |               +0
    #0: ToddCoxeter: diff 0.2.0          |             +0 |                +0 |               +0
    #0: ToddCoxeter:                     |         active |           missing |       % complete
    #0: ToddCoxeter: edges               |     57,907,200 |                 0 |           100.0%
    #0: ToddCoxeter: diff 0.2.25         |             +0 |                +0 |            +0.0%
    #0: ToddCoxeter: diff 0.2.0          |             +0 |                +0 |            +0.0%
    #0: ToddCoxeter: phase 0.2 = 24.099s | run 0 = 3min6s | all runs = 3min6s | elapsed = 3min6s
    ++++++++++++++++++++++++++++++++
    #0: ToddCoxeter: RUN 0 STOP (finished)
    #0: ToddCoxeter: run 0                |      lookahead |        lookbehind |              hlt |        felsch
    #0: ToddCoxeter: num. phases          |              1 |                 0 |                0 |             1
    #0: ToddCoxeter: time spent in phases |  24.099s (13%) |            - (0%) |           - (0%) | 2min42s (87%)
    #0: ToddCoxeter: phase 0.2 = 24.384s  | run 0 = 3min6s | all runs = 3min6s | elapsed = 3min6s
    The index of the subgroup is 7238400
    ```

:material-checkbox-marked-circle-outline: The computed index is the same as
the claimed index: $7,238,400$.

[libsemigroups_pybind11]:
  https://libsemigroups.github.io/libsemigroups_pybind11/index.html
