from libsemigroups_pybind11 import FroidurePin, word_graph, Transf, Dot, froidure_pin

# Part (a) cannot currently be done in python

# Part (b)
s = FroidurePin([Transf([0, 0, 2]), Transf([0, 1, 1])])

d = word_graph.dot(s.right_cayley_graph())
d.view()
d = word_graph.dot(s.left_cayley_graph())
d.view()


def dot_right_cayley_graph(
    s: FroidurePin, node_labels: list[str] = None, edge_labels: list[str] = None
) -> Dot:
    # TODO checks on node_labels and edge_labels

    if node_labels is None:
        node_labels = [
            "".join(chr(x + 97) for x in froidure_pin.factorisation(s, i))
            for i in range(s.size())
        ]
    if edge_labels is None:
        # TODO not this
        edge_labels = node_labels

    edge_colors = [
        "#00ff00",
        "#ff00ff",
        "#007fff",
        "#ff7f00",
        "#7fbf7f",
        "#4604ac",
        "#de0328",
        "#19801d",
        "#d881f5",
        "#00ffff",
        "#ffff00",
        "#00ff7f",
        "#ad5867",
        "#85f610",
        "#84e9f5",
        "#f5c778",
        "#207090",
        "#764ef3",
        "#7b4c00",
        "#0000ff",
        "#b80c9a",
        "#601045",
        "#29b7c0",
        "#839f12",
    ]
    d = word_graph.dot(s.right_cayley_graph())
    out_degree = s.number_of_generators()

    for i in range(s.size()):
        d.node(str(i)).add_attr("label", node_labels[i])

    start_table = '<<table border="0" cellpadding="2" cellspacing="0" cellborder="0">\n'
    end_table = "</table>>\n"

    def row(index: str, content: str) -> str:
        return f'<tr><td align="right" port="port{index}">{content}&nbsp;</td></tr>\n'

    label = (
        start_table
        + "".join(row(i, edge_labels[i]) for i in range(out_degree))
        + end_table
    )

    legend = Dot().name("legend").add_attr("node [shape=plaintext]")
    # HTML table for the head of the arrows in the legend
    legend.add_node("head").add_attr("label", label)

    # HTML table for the tail of the arrows in the legend
    label = start_table + "".join(row(i, "") for i in range(out_degree)) + end_table
    legend.add_node("tail").add_attr("label", label)

    for i in range(out_degree):
        legend.add_edge(f"head:port{i}:e", "tail:port{i}:w").add_attr(
            "color", edge_colors[i]
        ).add_attr("constraint", "false")
    d.add_subgraph(legend)
    return d
