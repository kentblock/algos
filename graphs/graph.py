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

    def get_other_vertex(self, vertex):
        """
        Helper to get the other vertex connected to the edge
        """
        if self.vertices[0] is vertex:
            return self.vertices[1]
        if self.vertices[1] is vertex:
            return self.vertices[0]


class Vertex:
    """
    Class for vertices
    """
    def __init__(self, label):
        self.label = label
        self.edges = []
    
    def _add_edge(self, edge):
        self.edges.append(edge)

    def __lt__(self, vertex):
        return self.label > vertex.label


    @property
    def neighbours(self):
        """
        Get all neighbouring vertices
        """
        neighbours = []
        for e in self.edges:
            neighbour = e.vertices[0]
            if neighbour is self:
                neighbour = e.vertices[1]
            neighbours.append((neighbour, e.weight))
        return neighbours

    def get_edge(self, other_vertex):
        """
        Helper returns edge to other vertex if there is one
        """
        for e in self.edges:
            if other_vertex in e.vertices and other_vertex is not self:
                return e

    def __str__(self):
        return f"{self.label}"

class Graph:
    """
    Class for undirected graph
    """
    def __init__(self, size=0):
        self.vertices = []
        if size:
            self.add_vertices(size)

    @property
    def edges(self):
        edges = []
        for v in self.vertices:
            for e in v.edges:
                if e not in edges:
                    edges.append(e)
        return edges

    def add_vertex(self):
        """
        Add a vertex to the graph
        """
        vertex = Vertex(len(self.vertices))
        self.vertices.append(vertex)
        return vertex
    
    def add_vertices(self, num_vertices):
        """
        Add multiple vertices to the graph
        """
        for _ in range(num_vertices):
            self.add_vertex()

    def add_edge(self, vertex1, vertex2, weight=1):
        """
        Add an edge to the graph
        """
        if isinstance(vertex1, int):
            vertex1 = self.get_vertex(vertex1)
        if isinstance(vertex2, int):
            vertex2 = self.get_vertex(vertex2)
        return Edge(vertex1, vertex2, weight)

    def get_vertex(self, label):
        """
        Get a vertex with a given label
        """
        for v in self.vertices:
            if v.label is label:
                return v

    def get_edge(self, vertex1, vertex2):
        """
        Get edge between vertex1 and vertex2 if there is one
        """
        if isinstance(vertex1, int):
            vertex1 = self.get_vertex(vertex1)
        if isinstance(vertex2, int):
            vertex2 = self.get_vertex(vertex2)
        return vertex1.get_edge(vertex2)

    def __str__(self):
        """
        Return graph represented by adjacency matrix
        """
        adj_matrix_str = "   "
        for i in range(len(self.vertices)):
            adj_matrix_str += f"{i} "
        adj_matrix_str += "\n"
        for _ in range(len(self.vertices)):
            adj_matrix_str += "__"
        adj_matrix_str += "___"
        adj_matrix_str += "\n"

        for i in range(len(self.vertices)):
            adj_matrix_str += f"{i} |"
            current_vertex = self.get_vertex(i)
            for j in range(len(self.vertices)):
                current_edge = current_vertex.get_edge(self.get_vertex(j))                
                if current_edge:
                    adj_matrix_str += f"{current_edge.weight} "
                else:
                    adj_matrix_str += "0 "
            adj_matrix_str += "\n"
        return adj_matrix_str

if __name__ == "__main__":

    test_graph = Graph(5)

    test_graph.add_edge(0, 4)
    test_graph.add_edge(1, 2)
    test_graph.add_edge(2, 3)
    test_graph.add_edge(0, 1)
    test_graph.add_edge(3, 1)

    print(f"Here is test_graph: \n{test_graph}")