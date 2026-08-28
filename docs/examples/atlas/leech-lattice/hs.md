# Higman-Sims group HS

The claims on this page come from
[https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/HS/](https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/HS/).

## Claim

$$
    \mathrm{HS} = \langle a,b \mid a^{2} = b^{5} = (ab)^{11} = (ab^{2})^{10} = [a,b]^{5} = [a,b^{2}]^{6} = [a,bab]^{3} = ababab^{2}ab^{-1}ab^{-2}ab^{-1}ab^{2}abab(ab^{-2})^{4} = ab (ab^{2}(ab^{-2})^{2})^{2} ab^{2}abab^{2} (ab^{-1}ab^{2})^{2} = abab(ab^{2})^{2}ab (ab^{-1})^{2} ab(ab^{2})^{2} ababab^{-2}ab^{-1}ab^{-2} = 1
\rangle
$$

with

$$
    |\mathrm{HS}| = 44,352,000.
$$

On this page, we verify that the above claimed presentation of the Higman-Sims
group HS defines a group of order $44,352,000$.

## The code

In [libsemigroups_pybind11][], the following script constructs the presentation
for HS and runs the Todd-Coxeter algorithm, whilst taking advantage of
techniques such as `lookahead` and `lookbehind`.

The code below took about 1 hour 20 minutes to run on a 2024 MacBook Pro M4 with
48GB of RAM:

<details markdown>
<summary>Code</summary>

```python
from datetime import timedelta

from libsemigroups_pybind11 import (
    KnuthBendix,
    Order,
    Presentation,
    ToddCoxeter,
    congruence_kind,
    presentation,
    to,
)
from libsemigroups_pybind11.words import parse_relations

# Setup the presentation object with the empty word and inverses, so it can represent a group
p = Presentation("abAB")
p.contains_empty_word(True)
presentation.add_inverse_rules(p, "ABab")

# Add the defining relations
presentation.add_rule(p, parse_relations("a^2"), "")
presentation.add_rule(p, parse_relations("b^5"), "")
presentation.add_rule(p, parse_relations("(ab)^11"), "")
presentation.add_rule(p, parse_relations("(ab^2)^10"), "")
presentation.add_rule(p, parse_relations("(a,b)^5"), "")
presentation.add_rule(p, parse_relations("(a,bab)^3"), "")
presentation.add_rule(p, parse_relations("(a,b^2)^6"), "")
presentation.add_rule(p, parse_relations("ababab^2aBaB^2aBab^2abab(aB^2)^4"), "")
presentation.add_rule(p, parse_relations("ab(ab^2(aB^2)^2)^2ab^2abab^2(aBab^2)^2"), "")
presentation.add_rule(p, parse_relations("abab(ab^2)^2ab(aB)^2ab(ab^2)^2ababaB^2aBaB^2"), "")
presentation.add_rule(p, parse_relations("(ababab^2aBaB^2ababaB)^2"), "")
presentation.add_rule(p, parse_relations("(ababab^2)^2ababaBabab(ab^2)^3ababaB"), "")
presentation.add_rule(p, parse_relations("ab(abab^2)^3ababab^2aBabaB^2abaBab^2"), "")

# The "coset enumerator" in libsemigroups is for semigroups and monoids, and
# has no optimizations for groups. To avoid longer relation words, we try to
# balance the length of the left- and right-hand sides.
presentation.balance(p, "abAB", "ABab")

# Remove the inverses to limit memory usage later.
presentation.replace_subword(p, "A", "a")
presentation.replace_subword(p, "B", "bbbb")
p.alphabet("ab")

# Reduce the rules in the presentation to avoid unnecessarily long relations
kb = KnuthBendix(congruence_kind.twosided, p)
kb.run_for(timedelta(microseconds=1))

# Create the ToddCoxeter instance using the reduced rules from the KnuthBendix
tc = ToddCoxeter(congruence_kind.twosided, to(kb, rtype=(Presentation,)))
tc.lookahead_extent(ToddCoxeter.options.lookahead_extent.full)
limit = 100_000_000

# If we just run Todd-Coxeter, this will very quickly use all the memory
# available, and seemingly only produces a graph with ~73% of the edges
# defined. So, we limit the number of nodes in the graph to "limit",
# and then repeatedly try to shrink the graph using lookaheads and lookbehinds.
# Lookbehinds are relatively slow, and so we only do this when lookahead isn't
# any longer shrinking the graph.
while not tc.finished():
    tc.run_until(lambda: tc.number_of_nodes_active() >= limit)
    num_lookaheads = 0
    while True:
        num_lookaheads += 1
        num_nodes = tc.number_of_nodes_active()
        tc.perform_lookahead()
        diff = num_nodes - tc.number_of_nodes_active()
        if diff <= 1_000_000:
            break
    if num_lookaheads == 1:
        tc.standardize(Order.shortlex)
        tc.perform_lookbehind()
        limit *= 1.1

print(f"The size of the group is {tc.number_of_classes()}")
```

</details>

## The output

The truncated output of the enumeration is below:

??? info "Truncated output from the Python script"

    ```
    #0: KnuthBendix: running for approx. 1µs
    -----------------------------------------------------------------------------------------------
    #0: KnuthBendix: locally confluent for:  1 / 13 ( 7.7%) rules (0s)
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #0: KnuthBendix: STARTING . . .
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #0: KnuthBendix: |A| = 2, |R| = 13, |u| + |v| ∈ [2, 57], ∑(|u| + |v|) = 519
    #0: KnuthBendix: rules           13 (active) |           16 (defined)
    #0: KnuthBendix: diff            -3 (active) |           +0 (defined)
    #0: KnuthBendix: time         122µs (total)  |    130,390/s (defined)
    -----------------------------------------------------------------------------------------------
    #0: KnuthBendix: |A| = 2, |R| = 13, |u| + |v| ∈ [2, 57], ∑(|u| + |v|) = 519
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #0: KnuthBendix: STOPPING -- timed out!
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #0: ToddCoxeter: running until predicate returns true or finished
    ++++++++++++++++++++++++++++++++
    #0: ToddCoxeter: RUN 0 START (strategy() = hlt)
    #0: ToddCoxeter: |A| = 2, |R| = 13, |u| + |v| ∈ [2, 57], ∑(|u| + |v|) = 519
    ++++++++++++++++++++++++++++++++
    #0: ToddCoxeter: HLT 0.0 START
    #0: ToddCoxeter: HLT 0.0.0        |       active |          killed |        defined
    #0: ToddCoxeter: nodes            |            1 |               0 |              1
    #0: ToddCoxeter:                  |       active |         missing |     % complete
    #0: ToddCoxeter: edges            |            0 |               2 |           0.0%
    #0: ToddCoxeter: time             | run 0 = 18µs | all runs = 18µs | elapsed = 49µs
    ++++++++++++++++++++++++++++++++
    #0: ToddCoxeter: HLT 0.0 STOP
    #0: ToddCoxeter: HLT 0.0.1        |       active |          killed |        defined
    #0: ToddCoxeter: nodes            |    5,000,150 |          85,626 |      5,085,776
    #0: ToddCoxeter: diff 0.0.0       |   +5,000,149 |         +85,626 |     +5,085,775
    #0: ToddCoxeter:                  |       active |         missing |     % complete
    #0: ToddCoxeter: edges            |    5,277,936 |       4,722,364 |          52.8%
    #0: ToddCoxeter: diff 0.0.0       |   +5,277,936 |      +4,722,362 |         +52.8%
    #0: ToddCoxeter: phase 0.0 = 87ms | run 0 = 87ms | all runs = 87ms | elapsed = 87ms
    [... lines omitted ...]
    ++++++++++++++++++++++++++++++++
    #0: ToddCoxeter: RUN 26 STOP (finished)
    #0: ToddCoxeter: run 26               |        lookahead |            lookbehind |                  hlt |       felsch
    #0: ToddCoxeter: num. phases          |                0 |                     0 |                    1 |            0
    #0: ToddCoxeter: time spent in phases |           - (0%) |                - (0%) |        8min50s (99%) |       - (0%)
    #0: ToddCoxeter: all runs             |        lookahead |            lookbehind |                  hlt |       felsch
    #0: ToddCoxeter: num. phases          |               26 |                     1 |                   10 |            0
    #0: ToddCoxeter: time spent in        |   40min59s (52%) |        28min20s (36%) |        9min26s (12%) |       - (0%)
    #0: ToddCoxeter: phase 26.1 = 8min53s | run 26 = 8min53s | all runs = 1h18min48s | elapsed = 1h19min23s
    #0: ToddCoxeter: lenlex standardizing the word graph, this might take a few moments!
    #0: ToddCoxeter: the word graph was lenlex standardized in 7.676s
    The size of the group is 44352000
    ```

:material-checkbox-marked-circle-outline: The computed size of the group matches
the size of the group provided on the ATLAS: $44,352,000$

Below is a visualisation of the computation as it progressed:

<figure style="margin-top: 0;">
  <div style="overflow: hidden;">
    <video autoplay loop muted playsinline
           style="display: block; width: 100%;
                  margin-top: -10%; margin-bottom: -5%;">
      <source src="../hs.mp4" type="video/mp4">
    </video>
  </div>
  <figcaption style="margin-top: 0;">
    Progress of the Todd–Coxeter computation.
  </figcaption>
</figure>
