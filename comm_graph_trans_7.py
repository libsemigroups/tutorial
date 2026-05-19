# You only need to have python and the igraph package installed, you can do
# this by doing

# pip install igraph

import json
import igraph as ig

n = 7
with open(f"comm-graph-trans-{n}.txt") as f:
    edges = json.load(f)
g = ig.Graph(n=n**n, edges=edges, directed=False)

g.clique_number()  # returns 82 when n = 7
