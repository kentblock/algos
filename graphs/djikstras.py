# Implemetation of Djikstra's algorithm for practice
import heapq
from graph import Graph, Vertex


def update_pq(pq, vertex, new_weight, current):
    """
    Update pq if new weight is less than current
    """
    for i in range(len(pq)):
        weight, v, prev = pq[i]
        if v is vertex and weight > new_weight:
            pq[i] = (new_weight, v, current)

def find_shortest_path(graph, source):
    """
    Djikstra's algorithm to find all shortest paths from source vertex
    """
    shortest_paths = []
    visited = []
    pq = []
    for v in graph.vertices:
        if v is not source:
            pq.append((MAX_WEIGHT + 1, v, None))
        else:
            pq.append((0, v, None))

    while pq:
        current_path_weight, current, prev_vertex = heapq.heappop(pq)
        visited.append(current)
        for (v, weight) in current.neighbours:
            if v not in visited:
                update_pq(pq, v, weight + current_path_weight, current)
        heapq.heapify(pq)
        shortest_paths.append((current, current_path_weight, prev_vertex))
    return shortest_paths

if __name__ == "__main__":
    """
    TESTING
    """
    MAX_WEIGHT = 10
    GRAPH_SIZE = 5
    SOURCE = 0
    test_graph = Graph(GRAPH_SIZE)
    test_graph.add_edge(0, 1, 6)
    test_graph.add_edge(0, 3, 1)
    test_graph.add_edge(1, 3, 2)
    test_graph.add_edge(1, 2, 5)
    test_graph.add_edge(1, 4, 2)
    test_graph.add_edge(2, 4, 5)
    test_graph.add_edge(3, 4, 1)
    print(test_graph)
    
    shortest_paths = find_shortest_path(
        test_graph,
        test_graph.get_vertex(SOURCE)
    )
    for item in shortest_paths:
        print(
            f"vertex: {item[0]} shortest_path: {item[1]} prev_vertex: {item[2]}"
        )
