# Worksheet

This page contains some exercises for computing some things using `libsemigroups_pybind11`.

1. Let $J_n$ denote the Jones monoid of degree $n$, and

    ![An element of the Jones monoid](../images/bipartition.png)

    be a bipartition of degree 14.

    1. How many elements does $J_{14}$ contain?
    2. How many idempotent elements does $J_{14}$ contain?
    3. How many idempotent elements does the Green's
       $\mathscr{D}$-class of $x$ in $J_{14}$ contain?
    4. How many idempotent elements $e$ such that $7$ is in the same part as 
       a negative integer does the Green's $\mathscr{D}$-class of $x$ in $J_{14}$ contain?

??? hint

    You can define $J_{14}$ as a finitely presented monoid in `libsemigroups_pybind11` by doing:

    ```python
    from libsemigroups_pybind11.presentation import examples
    examples.temperley_lieb_monoid(14)
    ```
    
    You can also define the generating set and the corresponding monoid with:

    ```python
    from libsemigroups_pybind11 import Bipartition, FroidurePin


    def jones_identity(n):
        if n < 0:
            raise ValueError("the argument (an int) is not >= 0")

        return Bipartition([[i, -i] for i in range(1, n + 1)])


    def jones_generators(n):
        if n < 0:
            raise ValueError("the argument (an int) is not >= 0")

        gens = []
        for i in range(1, n):
            part = [[i, i + 1], [-i, -i - 1]]
            part.extend([j, -j] for j in range(1, i))
            part.extend([j, -j] for j in range(i + 2, n + 1))
            gens.append(Bipartition(part))
        return gens


    def jones_monoid(n):
        return FroidurePin([jones_identity(n)] + jones_generators(n))
    ```
