class graph:
  def __init__(self, graph_dict = None):
    if graph_dict is None:
      graph_dict = {}
    self.graph_dict = graph_dict 
  
  # nodes
  def return_nodes_list(self):
    return list(self.graph_dict.keys())

  # edges
  def return_edges(self):
    return self.list_edges()

  def list_edges(self):
    edges = []
    for key in self.graph_dict:
      for value in self.graph_dict[key]:
        if {value, key} not in edges:
          edges.append({key, value})
    return edges
