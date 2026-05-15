# The GAP session and GAP scripts

In this section we describe the basics of interacting with GAP and writing GAP scripts.
We recommend the
[GAP software carpentries lesson](https://carpentries-incubator.github.io/gap-lesson/index.html) to those interested
in learning more about GAP itself, see also the 
[GAP tutorial](https://docs.gap-system.org/doc/tut/chap0_mj.html). Here we give a very condensed overview.

## The GAP prompt

After installing GAP and the `Semigroups` package as described in the
[Installation](../install) section, you should be able to start GAP
from your terminal simply by typing `gap`++enter++[^1]. If GAP has been installed correctly,
you should see a the GAP banner followed by the _GAP prompt_ `gap> ` similar to
the following:

```gap-repl title="GAP startup screen"
 ┌───────┐   GAP 4.16.0-beta1-14-g2489735-dirty built on 2026-05-08 11:09:24+0100
 │  GAP  │   https://www.gap-system.org
 └───────┘   Architecture: aarch64-apple-darwin25-default64-kv10
 Configuration:  gmp 6.3.0, GASMAN, readline
 Loading the library and packages ...
 Packages:   AClib 1.3.3, Alnuth 3.2.1, AtlasRep 2.1.11, AutoDoc 2026.05.03, AutPGrp 1.11.1, 
             Browse 1.8.22, CaratInterface 2.3.9, CRISP 1.4.8, Cryst 4.1.31, CrystCat 1.1.11, 
             CTblLib 1.3.11, curlInterface 2.4.3, FactInt 1.6.3, FGA 1.5.0, Forms 1.2.14, 
             GAPDoc 1.6.7, genss 1.6.9, IO 4.9.3, IRREDSOL 1.4.4, LAGUNA 3.9.7, orb 5.1.0, 
             PackageManager 1.6.3, Polenta 1.3.11, Polycyclic 2.18, PrimGrp 4.0.2, 
             RadiRoot 2.9, recog 1.4.4, ResClasses 4.7.4, SmallGrp 1.5.4, Sophus 1.27, 
             SpinSym 1.5.2, StandardFF 1.0, TomLib 1.2.11, TransGrp 3.6.5, utils 0.94
 Try '??help' for help. See also '?copyright', '?cite' and '?authors'
gap> 
```

We can test that it is working by typing `1+1;`++enter++ in the prompt. When doing so, we are greeted with
the answer `2`:

```gap-repl
gap> 1+1;
2
```

Note that every expression in GAP must be terminated by a semicolon `;`, otherwise GAP will assume
that more input is coming, and drop us into a _continuation prompt_ `> `:

```gap-repl
gap> 1+1
> 
```

Writing the missing semicolon `;`++enter++ will cause the expression to be evaluated:

```gap-repl
gap> 1+1
> ;
2
```

The program we are interacting with is called the GAP _REPL_: **R**ead **E**valuate **P**rint **L**oop.
As the name suggests, it first reads user input from the prompt, then it evaluates this input by performing
computation, then it prints the results of the computation and finally it repeats this behavior in a loop,
returning to the read step. We will later see a different interaction model via GAP scripts, but the REPL
is a good way to experiment and may be preferable when working with the worksheets later on.

You can quit the GAP REPL by typing `#!gap quit;`++enter++.

### The break loop

Occasionally you may encounter an error by attempting to perform an unsupported computation, or due to
a bug in some other method. This will drop you into the _break loop_, e.g. trying to add a number
and a string will cause such an error:

```gap-repl
gap> 1 + "a";
Error, no method found! For debugging hints type ?Recovery from NoMethodFound
Error, no 1st choice method found for `+' on 2 arguments
called from read-eval loop at *stdin*:23
type 'quit;' to quit to outer loop
brk>
```

The error message `Error, no method found!` indicates that GAP does not have a method implemented for adding
the number `1` and the string `"a"` (what would it even mean to add a number and a letter?), so it drops
us into the break loop, indicated by the `#!gap-repl brk> ` prompt, for debugging. To exit this loop, we can simply
`#!gap quit;`++enter++, which will bring us back to the GAP prompt `gap> `:

```gap-repl
gap> 1 + "a";
Error, no method found! For debugging hints type ?Recovery from NoMethodFound
Error, no 1st choice method found for `+' on 2 arguments
called from read-eval loop at *stdin*:23
type 'quit;' to quit to outer loop
brk> quit;
gap> 
```

We can now proceed as normal.
See the [Main loop and Break loop](https://docs.gap-system.org/doc/ref/chap6_mj.html) section of the
GAP reference manual for more details about the break loop and the main loop.

### The help system

GAP and the `Semigroups` package implement many different functions. What a function does may not
always be clear from its name, and it may be necessary to read the _documentation_ describing its
functionality. This can be done directly from the GAP REPL via the _help system_.
To learn more about a function, simply prepend a question mark `?` to its name.
For example, to learn more about the factorial function `Factorial` we type
`#!gap ?Factorial`++enter++ in the GAP prompt:

```
gap> ?Factorial
16.1-1 Factorial
  
  ‣ Factorial( n ) ───────────────────────────────────────────────────────────────── function
  
  returns the factorial n! of the positive integer n, which is defined as the product 1 ⋅ 2 ⋅
  3 ⋯ n.
  
  n!  is  the number of permutations of a set of n elements. 1 / n! is the coefficient of x^n
  in the formal series exp(x), which is the generating function for factorial.
  
  ────────────────────────────────────────  Example  ────────────────────────────────────────
    gap> List( [0..10], Factorial );
    [ 1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800 ]
    gap> Factorial( 30 );
    265252859812191058636308480000000
  ───────────────────────────────────────────────────────────────────────────────────────────
  
  PermutationsList (16.2-12) computes the set of all permutations of a list.
  -- <space> page, <n> next line, <b> back, <p> back line, <q> quit --
```

This opens the manual entry for `Factorial`, which describes the functionality of `Factorial`.
Note the instructions at the bottom for navigation: the ++space++ key moves to the next page,
the ++n++ key moves to the next line, the ++b++ key moves to the previous page, the ++p++
key moves to the previous line and the ++q++ key quits the help system. So press ++q++ to
quit, this should bring you back to a `gap> ` prompt.

Sometimes there are multiple places in the documentation that might be relevant, for example
typing `?Sum` yields:

```
gap> ?Sum
│   Choose an entry to view, 'q' for none (or use ?<nr> later):                                   │
│[1]   Reference: Sum                                                                             │
│[2]   Reference: Sum and Intersection of Pcgs                                                    │
│[3]   Reference: SumOp                                                                           │
│[4]   Reference: SumX                                                                            │
│[5]   Reference: SumIntersectionMat                                                              │
│[6]   Reference: SumFactorizationFunctionPcgs                                                    │
│[7]   CAP (not loaded): SumOfMorphisms for IsCapCategoryObject, IsList, IsCapCategoryObject      │
│[8]   CAP (not loaded): SumWithKeys                                                              │
│[9]   HAP (not loaded): SumOfFpGModules                                                          │
│[10]  HAP (not loaded): SumOp
```

Since there are multiple different `Sum` operations implemented for different
objects, we are presented with a choice on which `Sum` function documentation
to view. The menu should be navigable with the ++up++ and ++down++ keys using
++enter++ to select the relevant entry. You can also quit this menu using the
++q++ key. Finally, if you quit out of this menu (or if you installed GAP without
the `readline` library), then you can still choose an entry using the `?<nr>` syntax.
For example typing `?Sum`++enter++ and then typing ++q++ followed by `?2`++enter++ should
open the documentation for the second entry `Reference: Sum and Intersection of Pcgs`.

Additionally, the [GAP reference manual](https://docs.gap-system.org/doc/ref/chap0_mj.html)
and [Semigroups reference manual](https://semigroups.github.io/Semigroups/doc/chap0_mj.html)
available online contain all the same information but in html form.
Each manual also has an _index section_,
[GAP reference manual index](https://docs.gap-system.org/doc/ref/chapInd_mj.html) and
[Semigroups reference manual index](https://semigroups.github.io/Semigroups/doc/chapInd_mj.html),
which contains list of links to the documentation of every documented function in the standard library
and the Semigroups package, respectively. These can be useful to find out if a
certain function is implemented or not.

See also the [help system section](https://docs.gap-system.org/doc/ref/chap2_mj.html) of the
GAP reference manual.

## An overview of GAP (part 1)

In this section we give an overview of the base functionality of the GAP programming language

!!! note
    This section is very brief, for a more in-depth overview of GAP see the
    [GAP software carpentries lesson](https://carpentries-incubator.github.io/gap-lesson/index.html), the
    [GAP tutorial](https://docs.gap-system.org/doc/tut/chap0_mj.html) as well as the
    [GAP language overview](https://docs.gap-system.org/doc/ref/chap4_mj.html)
    section of the reference manual for more details.

### Integers and fractions

In GAP integers are written in decimal like usual, e.g. `120;` is the number 120. Numbers can be added, subtracted,
multiplied and divided in the usual fashion, e.g.

```gap-repl
gap> 120;
gap> 120 + 130;
250
gap> 120 - 130;
-10
gap> 120 * 130;
15600
gap> 120 / 10;
12
```

Note that division does not result in a floating point number, more about that later. It is also possible to compute
powers via the exponentiation operator `^` and to get the remainder when dividing by `n` (residue mod `n`) using
the `mod` operator:

```gap-repl
gap> 2 ^ 4;
16
gap> 7 mod 4;
3
gap> 120 ^ 130;
19659025508399066716721705285419704785992969025546107032058060352342654085887963277416925487\
50814629717517691688878376859167333924540241674240000000000000000000000000000000000000000000\
000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
```

Note that GAP can handle even very large numbers without using numerical approximation. Similarly, dividing
whole numbers results in a rational as opposed to a floating point number. We need to use the `#!gap Float` command
to convert such a rational to a floating point number:

```gap-repl
gap> 100/114;
50/57
gap> Float(100/114);
0.877193
```

### Functions and calls

GAP implements many functions, for example the `#!gap Factorial` function which computes factorials. Functions are usually
named using [upper camel case](https://en.wikipedia.org/wiki/Camel_case), e.g.
`Factorial` or `IsomorphismSemigroups`. To call a function, simply provide it
with one or more arguments in brackets, e.g. `#!bash Factorial(5);` will
compute the factorial of 5.

```gap-repl
gap> Factorial(5);
120
gap> Factorial(100);
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
gap> Factorial(200);
7886578673647905035523632139321850622951359776871732632947425332443594499634033429203042840119846239041772121389196388302576427902426371050619266249528299311134628572707633\
1723739698894392244562145166424025403329186413122742829485327752424240757390324032125740557956866022603190417032406235170085879617892222278962370389737472000000000000000000\
0000000000000000000000000000000
```

Multiple arguments are separated using commas. For example the `Binomial` function takes two arguments `n` and `k`
and computes the binomial coefficient `n` choose `k`. We can call it as `Binomial(n, k);`, e.g.

```
gap> Binomial(10, 5);
252
```

### Lists

One can also create lists in GAP using the square brackets syntax. So, for example `#!gap [1, 3, 5, 7, 9];` would
be a `gap` list consisting of the odd numbers less than 10. As a shorthand, to create a list of all integers between
`a` and `b` we can use the range notation `#!gap [a .. b];`, e.g. the range
`#!gap [2 .. 10];` contains all integers between 2 and 10 inclusive.

```gap-repl
gap> [1, 3, 5, 7, 9];
[ 1, 3, 5, 7, 9 ]
gap> [2 .. 10];
[ 2 .. 10 ]
```

Lists can be nested and there is generally no limitation to what values they can hold.

```gap-repl
gap> [1, [2, 3], [4, 5, [7, 8]], 9, [10, 11]];
[ 1, [ 2, 3 ], [ 4, 5, [ 7, 8 ] ], 9, [ 10, 11 ] ]
```

### Variables, assignment and indexing

We can assign a value to a variable using the `#!gap :=` syntax. So, for example `x := 3;` would assign the value
3 to the variable `x`. We can then use `x` in expressions e.g. `#!gap x * x + 1;`.
Lists can also be assigned to variables, for example `#!gap A := [1, 3, 5, 7, 9];` will assign the list
`[1, 3, 5, 7, 9]` to `A`. We can access the `n`-th entry in `A` by typing
`#!gap A[n];`. For example `#!gap A[1];` will return `1` and `#!gap A[2];` will
return `3`. Note that unlike other programming languages, GAP is 1-indexed, meaning that the first element of
a list is at position `1`, not `0`. Finally, we can modify a list entry by assigning to it, e.g. `#!gap A[3] := 100;`
will change the third entry of `A` to be `100`.

```gap-repl
gap> x := 3;
3
gap> x;
3
gap> x * x + 1;
10
gap> A := [1, 3, 5, 7, 9];
[ 1, 3, 5, 7, 9 ]
gap> A[1];
1
gap> A[2];
3
gap> A[3] := 100;
100
gap> A;
[ 1, 3, 100, 7, 9 ]
```

### Strings and printing

A _string_ is a way of representing a word or phrase on the computer. In GAP they are denoted by quotation marks, e.g.
`"apple"` or `"Hello world!"`. Under the hood strings are just lists of characters, so we can index them in the samme manner
as lists.

```gap-repl
gap> "apple";
"apple"
gap> phrase := "Hello world!";
"Hello world!"
gap> phrase[1];
'H'
gap> phrase[2];
'e'
gap> phrase[6];
' '
gap> phrase[10];
'l'
gap> phrase[12];
'!'
```

Strings and other objects can be printed in gap using the `#!gap Print` function. Multiple items can be printed
by passing them as arguments to `#!gap Print`. Finally, when printing we should usually end the command with the
newline character `"\n"`, otherwise subsequent text will be printed on the same line as our text.

```gap-repl
gap> x := 3;
3
gap> Print("The value of x is ", x, "\n");
The value of x is 3
gap> name := "Andy";
Andy
gap> Print("Hello ", name, " how are you?\n");
Hello Andy how are you?
```

### Comparison operators and booleans

GAP supports comparison functions for objects. We can check if two values are equal using the `=` operator, e.g. 
`1 = 1` will return `#!gap true` while `#!gap 1 = 10` will return `#!gap false`. Note that the `=` operator for
comparisons is different than the `:=` operator for assignment. To check if two
element differ we can use the `<>` operator, so that `1 <> 1` is `#!gap false` and `1 <> 10` is `#!gap true`.
Note that the `!=` operation that is common in other languages is **not** present in GAP and so `<>` should be used
instead. Finally, the `<`, `<=`, `>`, `>=` operators implement the inequality
operators "less than", "less than or equal to", "greater than" and "greater
than or equal to", respectively. The values `true` and `false` returned by these operators are called booleans.

```gap-repl
gap> 1 = 1;
true
gap> 1 = 10;
false
gap> 1 <> 1;
false
gap> 1 <> 10;
true
gap> 1 > 10;
false
gap> 1 < 10;
true
gap> 1 < 1;
false
gap> 1 <= 1;
true
```

### Comments

In GAP, one can indicate a code comment using the number sign `#`. Once a `#`
is encountered, every symbol until the end of the line is ignored. This can be
useful to describe what the code is doing. For example

```gap-repl
gap> 1 + 1; # This is a comment and has no impact on the computation
2
```

## GAP scripts

Using the GAP REPL is very nice for quick prototyping and single line code execution.
However, for more advanced GAP constructs such as conditionals, loops and functions,
covered in the [next section](#an-overview-of-gap-part-2), using the REPL can quickly
become cumbersome. 

It is therefore recommended to store more involved computations in a _GAP script_ file.
This is simply a text file with a `.g` extension that contains GAP code. For example,
using your text editor of choice, create a text file named `example.g`[^2] with
the following contents:

```gap title="example.g"
a := 1 + 4;
result := Factorial(a * 2);
Print("Factorial is ", result, "\n");
```

Note that we do not need to type the `gap> ` prompt in the GAP script file. 

To execute the script file in `gap`, open `gap` and execute the `Read` command to read the `example.g` file:

```gap-repl
gap> Read("example.g");
Factorial is 3628800
```

If the `Read` command fails, make sure the `example.g` file is in
the same directory that you open `gap` in[^3]. Note that, unlike in the REPL,
only the output of the `Print` commands is printed.

To make editing GAP script files slightly nicer, we recommend setting up a text editor for GAP file editing.
For editor support, see the
[relevant GAP system FAQ section](https://www.gap-system.org/faq/#where-is-the-gap-file-editor-how-do-i-save-gap-programs).
The [Kate editor](https://kate-editor.org/) is likely the simplest editor with built-in support for GAP.
Alternatively, [neovim](), [VSCode]() and [vim]() are well supported too, though you will need
to perform additional setup steps as per the FAQ.

## An overview of GAP (part 2)

In this section we cover conditionals, loops and function definitions in GAP.
All our code examples will now be of GAP script files, instead of the REPL, and can
be executed as described in the [GAP scripts](#gap-scripts) section.
We will indicate the output of executing the script with a comment `#!gap # Returns: ...`
at the end of the script.

### Conditionals

In programming, we may want to conditionally execute some code, depending on the
result of a prior computation.
GAP support conditional code execution using the `#!gap if condition then code; fi;` construct,
which executes the `code` expression if the `condition` is `true`, and does nothing otherwise, e.g.

```gap title="example.g"
if 1 > 10 then
  Print("1 > 10\n");
fi; # Does nothing because the condition fails

if 1 < 10 then
  Print("1 < 10\n");
fi; # Prints because the condition holds

# Result:
#  1 < 10
```

Here the fist condition `#!gap 1 > 10` does not hold, so the if statement ignores the
`Print` and nothing is printed. However the second condition holds and so the
`Print` statement is executed and `#!gap 1 < 10` is printed. Note also the use of
the continuation prompt `> ` to input code across multiple lines, it is often much
more readable to input `if` statements like this.
Every `if` statement must be closed by
an `fi;` statement.
It is also customary to indent the body of an if statement by 2 spaces, to provide visual
separation.

A variation, the `#!gap if condition then code1; else code2; fi;` construct allows us to
conditionally execute 1 of 2 _branches_ depending on whether the condition is true or not, e.g.

```gap title="example.g"
if 1 > 10 then
  Print("1 > 10\n"); # Does not print because the condition is false
else
  Print("1 < 10\n"); # Prints because the condition is false
fi;

# Result:
#  1 < 10
```

A final variation, the
`#!gap if condition1 then code1; elif condition2 then code2; else code3; fi;`
construct will execute `code1` if `condition1` holds,
otherwise it will execute `code2` if `condition2` holds, and finally it will
execute `code3` if neither `condition1` nor `condition2` holds.
An arbitrary number of `elif` clauses are allowed, in which case every
subsequent condition is tested only if all the prior ones fail, and the final
`else` clause may be omitted, in which case the if statement does nothing if all
conditions fail. E.g.

```gap title="example.g"
if 1 > 10 then
  Print("1 > 10\n"); # Conditions fails so nothing printed
elif 2 > 10 then
  Print("2 > 10\n"); # Condition fails no nothing printed
elif 11 > 10 then
  Print("11 > 10\n"); # Conditions holds so 11 > 10 printed
elif 12 > 10 then
  Print("12 > 10\n"); # Even though the condition holds, since an
                      # earlier condition holds, this line is not printed
else
  Print("All conditions failed!\n"); # Since an earlier condition held,
                                     # this line is not printed either.
fi;

# Result:
#  11 > 10
```

### Loops

We may want to repeatedly execute some code in a loop. In GAP this can be
done using the `for` and `while` loops.

The `#!gap for element in collection do code; od;` construct allows us to
execute the statement `code` where the variable `element` varies over
the elements of `collection`. For example, we the following for loop
prints all the elements of the list `A`:

```gap title="example.g"
A := [1, 3, 5, 7, 9];
for x in A do
  Print("x = ", x, "\n");
od;

# Result:
#   x = 1
#   x = 3
#   x = 5
#   x = 7
#   x = 9
```

Every `for` statement must be closed by a `od;` statement. As with `if` statements,
the body of the for loop gets indented 2 spaces.

The `for` loop
can also be useful when we want to repeat a certain action a number of times
that is previously known. For example, the following `for` loop adds
up the first `n` odd numbers:

```gap title="example.g"
n := 10;
x := 0;
for y in [1 .. n] do
  x := x + 2 * y - 1;
od;
Print(x, "\n");

# Result:
#   100
```

The `#!gap while condition do code; od;` construct will execution the `code` expresssion
until `condition` becomes `false`. For example, the following while loop
counts down from `10`:

```gap title="example.g"
n := 10;
while n > 0 do
  Print(n, "\n"); # Print n
  n := n - 1; # Decrease n by one
od;

# Result:
#  10
#  9
#  8
#  7
#  6
#  5
#  4
#  3
#  2
#  1
```

As with the `for` statement, we must close a `while` loop with an `od;` statement.
It is once again customary to indent the body of the `while` loop 2 spaces.

The `while` loop is useful when you do not know in advance how many iterations a certain
piece of code should be executed for. For example, the
[Collatz function](https://en.wikipedia.org/wiki/Collatz_conjecture) is a function on
the natural which, given a number `n`, divides `n` by two if `n` is even, and otherwise
it multiplies `n` by 3 and adds 1, i.e.

\[
  f(n) =
  \begin{cases}
    \frac{n}{2} & \text{if }n\text{ is even}\\
    3n + 1 & \text{otherwise}
  \end{cases}
\]

It is conjectured that applying this function repeatedly
to any starting number eventually reaches the number 1, but as of yet this remains an
open problem. We can use a `while` loop to implement our own Collats conjecture verifier:

```gap title="collatz.g"
n := 928; # Set some intial value for n
while n <> 1 do # Repeat the Collatz function application until the value is 1
  Print(n, "\n"); # Print n so we see how the number changes as we iterate
  if n mod 2 = 0 then # Check if n is even
    n := n / 2; # If so then divide by 2
  else
    n := n * 3 + 1; # If its odd then multiply by 3 and add 1
  fi;
od;
Print(n, "\n"); # Print n at the end to check its equal to 1

# Result:
#   928
#   464
#   232
#   116
#   58
#   29
#   88
#   44
#   22
#   11
#   34
#   17
#   52
#   26
#   13
#   40
#   20
#   10
#   5
#   16
#   8
#   4
#   2
#   1
```

Note that all the previous constructs: `if`, `for` and `while` can be nested within each other,
as we just saw in the Collatz example.

### Nested loops and early termination

It is often useful to iterate over multiple variables to search for examples or counterexamples, and to
terminate the search early once an example is found. This can be done using nested loops and the
`#!gap break;` statement respectively.

As an example, we consider the question of verifying if a given multiplication table defines
a semigroup. In order to do this we need to verify that the associativity axiom
$\forall x, y, z \in S, x(yz) = (xy)z$ holds.

In GAP, the multiplication table can be represented using a list of lists.
For example the multiplication table 

\[
\begin{array}{c|cccc}
\cdot & 1 & 2 & 3 & 4 \\
\hline
1 & 2 & 2 & 4 & 4 \\
2 & 3 & 2 & 3 & 3 \\
3 & 3 & 1 & 1 & 3 \\
4 & 4 & 4 & 1 & 3 \\
\end{array}
\]

could be encoded via the nested list:

```gap
table := [
  [2, 2, 4, 4],
  [3, 2, 3, 3],
  [3, 1, 1, 3],
  [4, 4, 1, 3]
];
```

We can look up the value of \(x \cdot y\) via double indexing `#!gap table[x][y]`.
To check if the table defines a semigroup, we use nested loops:

```gap title="associativity.g"
table := [
  [2, 2, 4, 4],
  [3, 2, 3, 3],
  [3, 1, 1, 3],
  [4, 4, 1, 3]
];
n := Length(table); # The Length functions gives us the number of entries
                    # in a list, in this case the number of rows.
is_semigroup := true; # Initially we assume the table defines a semigroup
for x in [1 .. n] do # Iterate over x
  for y in [1 .. n] do # Iterate over y
    for z in [1 .. n] do # Iterate over z
      if table[x][table[y][z]] <> table[table[x][y]][z] then # check if x * (y * z) = (x * y) * z
        Print("Failed with x = ", x, ", y = ", y, ", z = ", z, "\n");
        is_semigroup := false; # We found a counterexample to the associativity axiom so 
                               # the table does not define a semigroup
      fi;
    od;
  od;
od;

if is_semigroup then
  Print("Table defines a semigroup\n");
else
  Print("Table does not define a semigroup\n");
fi;

# Result:
#   Failed with x = 1, y = 1, z = 1
#   Failed with x = 1, y = 1, z = 3
#   Failed with x = 1, y = 1, z = 4
#   Failed with x = 1, y = 2, z = 1
#   Failed with x = 1, y = 2, z = 3
#   Failed with x = 1, y = 2, z = 4
#   Failed with x = 1, y = 3, z = 2
#   Failed with x = 1, y = 3, z = 3
#   Failed with x = 1, y = 3, z = 4
#   Failed with x = 1, y = 4, z = 3
#   Failed with x = 1, y = 4, z = 4
#   Failed with x = 2, y = 1, z = 1
#   Failed with x = 2, y = 1, z = 2
#   Failed with x = 2, y = 1, z = 3
#   Failed with x = 2, y = 3, z = 2
#   Failed with x = 2, y = 3, z = 3
#   Failed with x = 2, y = 4, z = 2
#   Failed with x = 2, y = 4, z = 3
#   Failed with x = 3, y = 1, z = 1
#   Failed with x = 3, y = 1, z = 3
#   Failed with x = 3, y = 2, z = 1
#   Failed with x = 3, y = 2, z = 2
#   Failed with x = 3, y = 2, z = 3
#   Failed with x = 3, y = 2, z = 4
#   Failed with x = 3, y = 3, z = 1
#   Failed with x = 3, y = 3, z = 2
#   Failed with x = 3, y = 3, z = 3
#   Failed with x = 3, y = 3, z = 4
#   Failed with x = 3, y = 4, z = 2
#   Failed with x = 3, y = 4, z = 3
#   Failed with x = 3, y = 4, z = 4
#   Failed with x = 4, y = 1, z = 3
#   Failed with x = 4, y = 2, z = 1
#   Failed with x = 4, y = 2, z = 4
#   Failed with x = 4, y = 3, z = 1
#   Failed with x = 4, y = 3, z = 2
#   Failed with x = 4, y = 3, z = 4
#   Failed with x = 4, y = 4, z = 2
#   Failed with x = 4, y = 4, z = 3
#   Failed with x = 4, y = 4, z = 4
#   Table does not define a semigroup
```

So the table does not define a semigroup, and there are multiple triples $x, y, z$ for which
associativity fails. However, the computation is a bit wasteful, since we can conclude that
the table does not define a semigroup as soon as we find the first failing triple.
We want to stop the loop early somehow. This is precisely what the `#!gap break;`
statement does: as soon as this statement is encountered, the innermost loop is stopped.

```gap title="associativity.g"
table := [
  [2, 2, 4, 4],
  [3, 2, 3, 3],
  [3, 1, 1, 3],
  [4, 4, 1, 3]
];
n := Length(table);
is_semigroup := true;
for x in [1 .. n] do
  for y in [1 .. n] do
    for z in [1 .. n] do
      if table[x][table[y][z]] <> table[table[x][y]][z] then
        Print("Failed with x = ", x, ", y = ", y, ", z = ", z, "\n");
        is_semigroup := false;
        break; # Once we encounter this line, the z loop is stopped
      fi;
    od;

    if not is_semigroup then # Check if the table was disproven to be a semigroup
      break; # If so, stop the y loop
    fi;
  od;

  if not is_semigroup then # Check if the table was disproven to be a semigroup
    break; # If so, stop the z loop
  fi;
od;

if is_semigroup then
  Print("Table defines a semigroup\n");
else
  Print("Table does not define a semigroup\n");
fi;

# Result:
#   Failed with x = 1, y = 1, z = 1
#   Table does not define a semigroup
```

Note that with the `#!gap break;` statements, only a single counterexample is found, hence
the search is stopped early.

The `Semigroups` package offers a simpler way of checking if a multiplication table
defines a semigroup, which we will cover in [Worksheet 1](../worksheet1).

### Defining functions

Finally, we can use the `#!gap function(arguments) end;` construct to define a function
in GAP. This can be useful for factoring out commonly used functionality.

For example, we could take our code for the Collatz function iteration
from the [Loops](#loops) section into a function `Collatz` as follows:

```gap title="collatz.g"
Collatz := function(n) # We declare n as a variable to the function
  while n <> 1 do
    Print(n, "\n");
    if n mod 2 = 0 then
      n := n / 2;
    else
      n := n * 3 + 1;
    fi;
  od;
  return n; # The return statement returns n as the output value of the function
end;
```

Note that, the `function` statement needs to be ended with an `#!gap end;` statement.
It is once again customary to indent the body of the function with two spaces.

Now in the GAP REPL, after `Read`ing the file, we can use the `Collatz` function as
follows:

```gap-repl
gap> Read("collatz.g");
gap> Collatz(10);
10
5
16
8
4
2
1
gap> Collatz(20);
20
10
5
16
8
4
2
1
```

Note that we can call the `Collatz` function with different values without needing to
rewrite the code.

Similarly, we can convert the associativity checking code from the
[Nested loops and early termination](#nested-loops-and-early-termination) section
into a function `IsAssociativeTable` as follows:

```gap title="associativity.g"
IsAssociativeTable := function(table)
  n := Length(table);
  for x in [1 .. n] do
    for y in [1 .. n] do
      for z in [1 .. n] do
        if table[x][table[y][z]] <> table[table[x][y]][z] then
          Print("Failed with x = ", x, ", y = ", y, ", z = ", z, "\n");
          # As soon as a return statement is encountered, the value
          # is returned and no further function coe is executed, so
          # we do not need to use break statements here.
          return false;
        fi;
      od;
    od;
  od;
  # We can only reach this line if no counterexample is found, in which
  # case the table is associative.
  return true;
end;
```

If we try to `Read` this file, however, we are greeted with some warnings:

```gap-repl
gap> Read("associativity.g");
Syntax warning: Unbound global variable in associativity.g:2
  n := Length(table);
  ^
Syntax warning: Unbound global variable in associativity.g:3
  for x in [1 .. n] do
      ^
Syntax warning: Unbound global variable in associativity.g:3
  for x in [1 .. n] do
                 ^
Syntax warning: Unbound global variable in associativity.g:4
    for y in [1 .. n] do
        ^
Syntax warning: Unbound global variable in associativity.g:4
    for y in [1 .. n] do
                   ^
Syntax warning: Unbound global variable in associativity.g:5
      for z in [1 .. n] do
          ^
Syntax warning: Unbound global variable in associativity.g:5
      for z in [1 .. n] do
                     ^
```

this is because the variables, `x, y, z` and `n` that are used in the function
have not been declared for use within the function. Essentially, every function
definition is allowed to have its own local variables, which GAP
only uses within the context of the function, however we need to declare these
using the `local` statement at the start of the function declaration:

```gap title="associativity.g"
IsAssociativeTable := function(table)
  # Declaring local variables means they won't interfere with definitions
  # of x, y, z and n outside the function.
  local x, y, z, n;
  n := Length(table);
  for x in [1 .. n] do
    for y in [1 .. n] do
      for z in [1 .. n] do
        if table[x][table[y][z]] <> table[table[x][y]][z] then
          Print("Failed with x = ", x, ", y = ", y, ", z = ", z, "\n");
          # As soon as a return statement is encountered, the value
          # is returned and no further function coe is executed, so
          # we do not need to use break statements here.
          return false;
        fi;
      od;
    od;
  od;
  # We can only reach this line if no counterexample is found, in which
  # case the table is associative.
  return true;
end;
```

In the GAP REPL we can then use the newly defined function as:

```gap-repl
gap> Read("associativity.g");
gap> IsAssociativeTable([[1, 2, 3], [2, 3, 1], [3, 1, 2]]);
true
gap> IsAssociativeTable([[2, 2, 4, 4], [3, 2, 3, 3], [3, 1, 1, 3], [4, 4, 1, 3]]);
Failed with x = 1, y = 1, z = 1
false
```

Finally, a function with multiple arguments can be defined by separating the arguments
with commas:

```gap title="example.g"
AddTwoNumbers := function(x, y)
  return x + y;
end;

# Running AddTwoNumbers(2, 3) returns 5
```

This concludes the basic overview of the GAP programming language.

[^1]:
    For Windows users, you should first type `ubuntu` to enter the Ubuntu Linux subsystem
    and only then type `gap`. This will be the case for all commands going forward, so
    make sure you are in the Ubuntu Linux subsystem whenever executing the commands.

[^2]:
    Windows users may need to enable the option to
    [show file extensions](https://support.microsoft.com/en-us/windows/common-file-name-extensions-in-windows-da4a4430-8e76-89c5-59f7-1cdbbc75cb01)
    in order to be able to correctly set the file extension to `.g`. 

[^3]:
    For Windows users, you need to make sure the files are located within the `WSL`
    filesystem. According to [this stack overflow answer](https://superuser.com/a/1791389),
    this directly can be accessed from Windows by typing
    `\\wsl.localhost\Ubuntu\home\{username}` in the Windows Explorer, substituting
    `{username}` for the username you chose when you first ran the `ubuntu` command.
    Files in this directory correspond to files in the `~` directory from the 
    WSL side.
