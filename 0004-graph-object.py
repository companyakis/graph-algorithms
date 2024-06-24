# let's create a graph object

g = graph(first_graph)

print("Nodes: ", g.return_nodes_list())

print("Edges: ", g.return_edges())

"""
Nodes:  ['A', 'B', 'C', 'D', 'E', 'F']

Edges:  [{'A', 'B'}, {'A', 'C'}, {'D', 'B'}, {'E', 'B'}, {'C', 'D'}, {'E', 'D'}, {'E', 'F'}]

"""
