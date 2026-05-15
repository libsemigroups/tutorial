# Finite, finitely generated and acting semigroups in GAP

This section provides information about how to compute with a finite or finitely generated
semigroup or monoid using the `Semigroups` package for GAP. We assume some basic familiarity
with the GAP programming language, see the [GAP: First Steps](session.md) section for
a basic overview if you do not yet feel comfortable with GAP.

GAP does provide some built-in functionality related to semigroups, see the reference manual

* [Chapter 51: Semigroups and Monoid](https://docs.gap-system.org/doc/ref/chap51_mj.html),
* [Chapter 52: Finitely Presented Semigroups and Monoids](https://docs.gap-system.org/doc/ref/chap52_mj.html),
* [Chapter 53: Transformations](https://docs.gap-system.org/doc/ref/chap53_mj.html) and
* [Chapter 54: Partial permutations](https://docs.gap-system.org/doc/ref/chap54_mj.html).

However, some functionality is missing and many of the algorithms
for semigroups as implemented in base GAP can be quite slow. The `Semigroups` package
significantly expands the available computational semigroup theory toolbox and provides
fast `C++` implementations of standard semigroup theory algorithms, such as the
[Froidure-Pin algorithm](https://semigroups.github.io/Semigroups/doc/chap6_mj.html#X7E2DE9767D5D82F7).

In order to load the `Semigroups` package simply add
```gap
LoadPackage("Semigroups");
```
at the start of your gap script, or execute this command at the start of your
GAP session.

!!! failure "If Semigroups fails to load"
    If you encounter an error when loading the `Semigroups` package,
    it may be due to the kernel module (the `C++` component powering `Semigroups`)
    not being compiled. Execute the command
    `#!gap SetInfoLevel(InfoPackageLoading, 4);` and attempt to load the package
    again. If you see an error similar to the following:
    ```gap-repl
    gap> SetInfoLevel(InfoPackageLoading, 4);
    gap> LoadPackage("Semigroups");
    #I  Semigroups: entering LoadPackage 
    #I  Semigroups: PackageAvailabilityInfo for version 5.5.4
    #I  Semigroups: the kernel module is not compiled, 
    #I              the package cannot be loaded.
    #I  Semigroups: PackageAvailabilityInfo: the AvailabilityTest function returned false
    #I  Semigroups: PackageAvailabilityInfo: no installed version fits
    #I  Semigroups: return from LoadPackage, package is not available
    fail
    ```
    This is an indication that you need to compile the kernel module.
    Please follow [Step 7 of the Standard Install instructions](install.md#common-installation-steps)
    to fix this error.

## Finite semigroups

In this section we showcase how one can construct and analyze certain kinds
of finite semigroups.

### Transformation semigroups

Before we delve into functions for analyzing semigroups, we first need to
construct some example to analyze. In this section we introduce one rich
family of examples, the _transformation semigroups_.

Recall that a _transformation_ of
degree $n$ is a function $f: \{1, \ldots, n\} \rightarrow \{1, \ldots, n\}$ and
the _full transformation semigroup_ of degree $n$ is semigroups
$\mathcal{T}_n$ consisting of all degree $n$ transformations under composition.

In GAP the function `#!gap FullTransformationSemigroup(n);` can be used to construct
the semigroup $\mathcal{T}_n$, and check some basic facts about it.

!!! note
    The code examples in this section will consist of two tabs: one labelled
    "GAP REPL" showcasing the output in an example GAP REPL session, and
    another labelled "GAP script" which contains the same code without the
    GAP REPL output, for easier copy-pasting into a GAP session.

=== "GAP REPL"
    ```gap-repl
    gap> T := FullTransformationSemigroup(3);
    <full transformation monoid of degree 3>
    gap> Size(T); # The order of T
    27
    gap> IsMonoid(T); # Is T a monoid?
    true
    gap> IsRegularSemigroup(T); # Is T regular?
    true
    gap> IsCommutativeSemigroup(T); # Is T commutative?
    false
    ```
=== "GAP script"
    ```gap
    T := FullTransformationSemigroup(3);
    Size(T); # The order of T
    IsMonoid(T); # Is T a monoid?
    IsRegularSemigroup(T); # Is T regular?
    IsCommutativeSemigroup(T); # Is T commutative?
    ```

As we discussed in the [Help system section](./session.md#the-help-system), to
learn more about any GAP function you can use the help operator `?` in the GAP
REPL, e.g.

```gap-repl
gap> ?FullTransformationSemigroup
  53.7-3 FullTransformationSemigroup
  
  ‣ FullTransformationSemigroup( n ) ─────────────────────────────────── function
  ‣ FullTransformationMonoid( n ) ────────────────────────────────────── function
  Returns:  The full transformation semigroup of degree n.
  
  If n is a positive integer, then FullTransformationSemigroup returns the monoid
  consisting  of  all  transformations  with  degree  at  most n, called the full
  transformation semigroup.
  
  The  full  transformation  semigroup  is  regular,  has  n ^ n elements, and is
  generated  by  any  set  containing transformations that generate the symmetric
  group on n points and any transformation of rank n - 1.
  
  FulTransformationMonoid is a synonym for FullTransformationSemigroup.
  
  ──────────────────────────────────  Example  ──────────────────────────────────
    gap> FullTransformationSemigroup( 1234 );
    <full transformation monoid of degree 1234>
  ───────────────────────────────────────────────────────────────────────────────
  -- <space> page, <n> next line, <b> back, <p> back line, <q> quit --
```

This can be especially helpful for understanding the functions we will use
going forward.

To display the elements of `T` we can use the GAP function `Elements`:

=== "GAP REPL"
    ```gap-repl
    gap> Elements(T);
    [ Transformation( [ 1, 1, 1 ] ), Transformation( [ 1, 1, 2 ] ), 
      Transformation( [ 1, 1 ] ), Transformation( [ 1, 2, 1 ] ), 
      Transformation( [ 1, 2, 2 ] ), IdentityTransformation, 
      Transformation( [ 1, 3, 1 ] ), Transformation( [ 1, 3, 2 ] ), 
      Transformation( [ 1, 3, 3 ] ), Transformation( [ 2, 1, 1 ] ), 
      Transformation( [ 2, 1, 2 ] ), Transformation( [ 2, 1 ] ), 
      Transformation( [ 2, 2, 1 ] ), Transformation( [ 2, 2, 2 ] ), 
      Transformation( [ 2, 2 ] ), Transformation( [ 2, 3, 1 ] ), 
      Transformation( [ 2, 3, 2 ] ), Transformation( [ 2, 3, 3 ] ), 
      Transformation( [ 3, 1, 1 ] ), Transformation( [ 3, 1, 2 ] ), 
      Transformation( [ 3, 1, 3 ] ), Transformation( [ 3, 2, 1 ] ), 
      Transformation( [ 3, 2, 2 ] ), Transformation( [ 3, 2, 3 ] ), 
      Transformation( [ 3, 3, 1 ] ), Transformation( [ 3, 3, 2 ] ), 
      Transformation( [ 3, 3, 3 ] ) ]
    ```
=== "GAP script"
    ```gap
    Elements(T);
    ```

Instead of representing transformations as functions, GAP uses a bespoke
`Transformation` object. A transformation $t$ is specified by providing
a list `A` such that the $i$-th entry `A[i]` is the image of the point $i$
under the transformation $t$. So, for example
`#!gap t := Transformation([1, 3, 3, 4]);` defines the transformation
`t \in \mathcal{T}_4`
such that $t(1) = 1, t(2) = t(3) = 3$ and $t(4) = 4$. We can
multiply transformations using the usual multiplication operator `*`.
Furthermore, we can obtain the image $t(x)$ of a point
$x \in \{1, \ldots, 4\}$ under $t$ via the power syntax `x ^ t`.

=== "GAP REPL"
    ```gap-repl
    gap> a := Transformation([1, 3, 3, 4]);
    Transformation( [ 1, 3, 3 ] )
    gap> b := Transformation([2, 3, 4, 1]);
    Transformation( [ 2, 3, 4, 1 ] )
    gap> a * b;
    Transformation( [ 2, 4, 4, 1 ] )
    gap> b * a;
    Transformation( [ 3, 3, 4, 1 ] )
    gap> 2 ^ a;
    3
    gap> 3 ^ b;
    4
    gap> 2 ^ (a * b);
    4
    gap> 2 ^ (b * a);
    3
    ```
=== "GAP script"
    ```gap
    a := Transformation([1, 3, 3, 4]);
    b := Transformation([2, 3, 4, 1]);
    a * b;
    b * a;
    2 ^ a;
    3 ^ b;
    2 ^ (a * b);
    2 ^ (b * a);
    ```

!!! note
    In fact, mathematically all transformations in GAP belong to
    the infinite transformation monoid $T_\mathbb{N}$ of transformations
    $f: \mathbb{N} \rightarrow \mathbb{N}$. GAP simply treats all points
    after the largest moved point of a transformation $t$ as fixed.
    This means that we can multiply two transformations acting
    on a different number of points, so e.g.
    `#!gap Transformation([2, 1]) * Transformation([3, 3, 4, 5]);`
    is valid. Similarly, `#!gap 10 ^ (Transformation([2, 1]));` is
    valid and returns `10`.

We can construct a semigroups generated by a set of transformations using the
`Semigroup` function:

=== "GAP REPL"
    ```gap-repl
    gap> a := Transformation([1, 3, 3, 4]);
    Transformation( [ 1, 3, 3 ] )
    gap> b := Transformation([2, 3, 4, 1]);
    Transformation( [ 2, 3, 4, 1 ] )
    gap> c := Transformation([1, 1, 2, 2]);
    Transformation( [ 1, 1, 2, 2 ] )
    gap> S := Semigroup([a, b, c]);
    <transformation semigroup of degree 4 with 3 generators>
    gap> Size(S); # All the usual semigroup functions should work
    128
    gap> IsRegularSemigroup(S);
    true
    gap> IsCommutativeSemigroup(S);
    false
    ```
=== "GAP script"
    ```gap
    a := Transformation([1, 3, 3, 4]);
    b := Transformation([2, 3, 4, 1]);
    c := Transformation([1, 1, 2, 2]);
    S := Semigroup([a, b, c]);
    Size(S); # All the usual semigroup functions should work
    IsRegularSemigroup(S);
    IsCommutativeSemigroup(S);
    ```





### Green's relations

TODO: Intro on what these are etc

<div class="grid" markdown>

  <div markdown>
  Recall that the _egg-box diagram_ of a semigroup is a visual representation
  of its Green's relations. In GAP we can display them using the `Splash` and
  `DotString` functions:

=== "GAP REPL"
    ```gap-repl
    gap> Splash(DotString(T, rec(maximal := true)));
    ```
=== "GAP script"
    ```gap
    Splash(DotString(T, rec(maximal := true)));
    ```

  The resulting egg-box diagram for $\mathcal{T}_3$ can be seen on the right.
  The large boxes labelled 1, 2 and 3 in the diagram correspond to Green's
  $\mathscr{D}$-classes of $\mathcal{T}_3$, the lines between them denote
  inclusion in the ordering on $\mathscr{D}$-classes induced by the Green's
  $\mathcal{J}$-relation.

  The rows of the boxes representing the $\mathscr{D}$-classes correspond to
  Green's $\mathscr{L}$-classes, the columns to Green's $\mathscr{R}$-classes.
  Finally, the cells of the boxes representing the $\mathscr{D}$-classes
  are the $\mathscr{H}$-classes of $\mathcal{T}_3$. Cells shaded in gray
  denote the group $\mathscr{H}$-classes, and they contain the [`StructureDescription`](https://docs.gap-system.org/doc/ref/chap39.html#X8199B74B84446971) of these groups.

  So, by visual inspection we can deduce that $\mathcal{T}_3$ has
  3 Green's $\mathscr{D}$-classes, furthermore, each $\mathscr{D}$-class
  contains a group $\mathscr{H}$-class, and is therefore a regular
  $\mathscr{D}$-class. Hence we can conclude that $\mathcal{T}_3$ is regular,
  just by visual inspection of the egg-box diagram.
  </div>

![The egg-box diagram of $\mathcal{T}_3$](../images/T3_egg_box.png){ align=right width=200rem }
/// caption
The egg-box diagram of $\mathcal{T}_3$.
///
</div>

### Multiplication tables

### Cayley graphs

### Finite inverse semigroups

### Semigroups of bipartitions

[TODO](https://semigroups.github.io/Semigroups/doc/chap3_mj.html)

## Finitely generated semigroups

### Semigroups of matrices over semirings

