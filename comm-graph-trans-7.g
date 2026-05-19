# The following assumes you have the Semigroups package for GAP installed as
# per:
#
# https://libsemigroups.github.io/tutorial/gap/install/

# If you try this for the first time, maybe try n := 5 or 6 first, just to
# check that it works.
n := 7;
S := FullTransformationMonoid(n);
# In the next line we construct the commuting graph, including the centre
# (identity). The idea is that we use the SymmetricGroup(n) acting on the list
# of elements of S by conjugation (represented by POW here), and the function
# {x, y} -> x * y = y * x says when there should be an edge between two nodes x
# and y. The idea here is that we compute the neighbours of one representative
# per orbit of the group under this action, and then compute the neighbours of
# the other elements in the orbit by conjugation. This turns out to be faster
# than the brute force approach.
D := Digraph(SymmetricGroup(n), AsListCanonical(S), POW, {x, y} -> x * y = y * x);

# For small values of n (<=5) you could at this point just do:
# CliqueNumber(D);
# This is too slow when n = 6 or 7 so we save the graph to a file and use
# python.

# In the next line we write the edges of the graph out into a file, this
# creates a very large file, but is fast, and allows us to create the graph in
# python relatively quickly too
FileString(StringFormatted("comm-graph-trans-{}.txt", n),
           String(DigraphEdges(D) - 1));
