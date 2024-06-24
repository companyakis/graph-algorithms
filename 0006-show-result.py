first_graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["B", "D", "F"],
    "F": ["E"]
}

g = graph(first_graph)

g.add_node("G")

g.add_edge({"G", "A"})

g.add_edge({"G", "B"})

print("Nodes: ", g.return_nodes_list())

print("Edges: ", g.return_edges())

"""
Nodes:  ['A', 'B', 'C', 'D', 'E', 'F', 'G']
Edges:  [{'A', 'B'}, {'A', 'C'}, {'A', 'G'}, {'D', 'B'}, {'E', 'B'}, {'C', 'D'}, {'E', 'D'}, {'E', 'F'}, {'G', 'B'}]
"""
