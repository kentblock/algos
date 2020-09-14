# Very basic implementation of a Graph class

class Edge:
    """
    Class for undirected weighted edges
    """
    def __init__(self, vertex1, vertex2, weight=1):
        self.weight = weight
        self.vertices = (vertex1, vertex2)
        vertex1._add_edge(self)
        vertex2._add_edge(self)


class Vertex:
    """
    Class for vertices
    """
    def __init__(self):
        self.edges = []
    
    def _add_edge(self, edge):
        self.edges.append(edge)


class Graph:
    """
    Class for undirected graph
    """
    def __init__(self):
        self.vertices = []

    @property
    def edges(self):
        edges = []
        for v in self.vertices:
            for e in v.edges:
                if e not in edges:
                    edges.append(e)
        return edges
 