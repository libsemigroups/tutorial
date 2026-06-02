# Verifying presentations in the ATLAS of Finite Groups

In this example, we will verify the validity of the presentations of the
sporadic groups as given in [this ATLAS][atlas].
In particular, where possible, we will use the Todd-Coxeter algorithm to check
that the size of group defined by the presentations is equal to the claimed
size. Where the claimed size of the group is very large, we will instead
calculate the size of small-index subgroups.

??? info "libsemigroups_pybind11 version"

    All examples provided on the subsequent subpages were run using
    libsemigroups_pybind11 version 1.4.4 on a laptop with a 13th Gen Intel(R)
    Core(TM) i7-13700H processor and 64 GB RAM.

??? info "Defining groups with monoid presentations"

    The presentations provided for the groups in the ATLAS are
    *group presentations*. This means that it is assumed that there is
    multiplicative identity $1$, and that each generator $a$ has an inverse
    $a^{-1}$ such that $aa^{-1} = a^{-1}a = 1$. In [libsemigroups_pybind11][],
    however, presentations are either *semigroup presentations* or
    *monoid presentations*, depending whether the relations of the presentation
    are allowed to contain the empty word $\varepsilon$. Therefore, we will need
    to add extra generators and relations to a monoid presentation to define a
    group.

    Suppose that a group $G$ is defined by the group presentation
    $\langle{A \mid R }\rangle_{\text{grp}}$. Then $G$ can also be defined by
    the monoid presentation
    $\langle{A \sqcup A^{-1} \mid R \cup R' }\rangle_{\text{mon}}$ where
    $A^{-1}$ is a set disjoint from $A$ containing letters that will be treated
    as inverses for the letters in $A$, and $R'$ is the set of relations of the
    form $aa^{-1} = \varepsilon$ and $a^{-1}a = \varepsilon$.

    In the subsequent subpages, we will use lowercase letters for the
    generators that are given in the presentations in the ATLAS, and their
    uppercase counterparts to represent their inverses. Therefore, many of our
    examples will in a similar way to:

    ```py
    from libsemigroups_pybind11 import presentation, Presentation
    p = presentation("abAB")
    p.contains_empty_word(True)
    presentation.add_inverse_rules(p, "ABab")
    ```

    The algorithms in [libsemigroups_pybind11][] were written for semigroups and
    monoids. This means that there are no group-specific optimisations.

The following tables summarise the results of this project. Click on a group
to see more information.

<div class="row">
  <div class="column">
    <div class="atlas-summary">
      <table>
        <tr>
          <th colspan="5">Mathieu groups</th>
        </tr>
        <tr>
          <td class="correct-size">
            <a href="mathieu/m11">M<sub>11</sub></a>
          </td>
          <td class="correct-size">
            <a href="mathieu/m12">M<sub>12</sub></a>
          </td>
          <td class="correct-size">
            <a href="mathieu/m22">M<sub>22</sub></a>
          </td>
          <td class="correct-index">
            <a href="mathieu/m23">M<sub>23</sub></a>
          </td>
          <td class="correct-index">
            <a href="mathieu/m24">M<sub>24</sub></a>
          </td>
        </tr>
      </table>
    </div>
    <div class="atlas-summary">
      <table>
        <tr>
          <th colspan="7">Leech lattice groups</th>
        </tr>
        <tr>
          <td class="could-not-verify"><a href="leech-lattice/hs">HS</a></td>
          <td>
            <a href="leech-lattice/j2">J<sub>2</sub></a>
          </td>
          <td class="no-presentation">Co<sub>1</sub></td>
          <td>
            <a href="leech-lattice/co2">Co<sub>2</sub></a>
          </td>
          <td class="no-presentation">Co<sub>3</sub></td>
          <td><a href="leech-lattice/mcl">McL</a></td>
          <td class="no-presentation">Suz</td>
        </tr>
      </table>
    </div>
    <div class="atlas-summary">
      <table>
        <tr>
          <th colspan="8">Monster sections</th>
        </tr>
        <tr>
          <td><a href="monster-sections/he">He</a></td>
          <td class="no-presentation">HN</td>
          <td class="no-presentation">Th</td>
          <td>
            <a href="monster-sections/fi22">Fi<sub>22</sub></a>
          </td>
          <td class="no-presentation">Fi<sub>23</sub></td>
          <td class="no-presentation">Fi<sub>24</sub>'</td>
          <td class="no-presentation">B</td>
          <td class="no-presentation">M</td>
        </tr>
      </table>
    </div>
    <div class="atlas-summary">
      <table>
        <tr>
          <th colspan="6">Pariahs</th>
        </tr>
        <tr>
          <td>
            <a href="pariahs/j1">J<sub>1</sub></a>
          </td>
          <td class="no-presentation">O'N</td>
          <td>
            <a href="pariahs/j3">J<sub>3</sub></a>
          </td>
          <td><a href="pariahs/ru">Ru</a></td>
          <td>
            <a href="pariahs/j4">J<sub>4</sub></a>
          </td>
          <td class="no-presentation">Ly</td>
        </tr>
      </table>
    </div>
    <div class="atlas-summary">
      <table>
        <tr>
          <th>Miscellaneous</th>
        </tr>
        <tr>
          <td><a href="misc/t">T</a></td>
        </tr>
      </table>
    </div>
  </div>

  <div class="column">
    <div class="atlas-summary">
      <table>
        <tr>
          <th>Legend</th>
        </tr>
        <tr>
          <td class="correct-size">
            The presentation defines a group of the correct size
          </td>
        </tr>
        <tr>
          <td class="correct-index">
            The presentation has a subgroup of the correct size
          </td>
        </tr>
        <tr>
          <td class="incorrect-size">
            The presentation defines a group of the incorrect size
          </td>
        </tr>
        <tr>
          <td class="could-not-verify">Todd-Coxeter did not terminate</td>
        </tr>
        <tr>
          <td class="no-presentation">No presentation is provided</td>
        </tr>
      </table>
    </div>
  </div>
</div>

[atlas]: https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/
[libsemigroups_pybind11]: https://libsemigroups.github.io/libsemigroups_pybind11/index.html
