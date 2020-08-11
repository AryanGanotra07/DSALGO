class Edge:
    def __init__(self, src, dest):
        self.src=src
        self.dest=dest
class Graph:
    def __init__(self, edges):
        self.adj = [[]for i in range(len(edges))]
        for edge in edges:
            self.adj[edge.src].append(edge.dest)
    def print(self):
        for src in range(len(self.adj)):
            for dest in self.adj[src]:
                print(f"({src} -> {dest}) ",end = "")
            print()


if __name__ == '__main__':

	# Input: Edges in a directed graph
	edges = [Edge(0, 1), Edge(1, 2), Edge(2, 0), Edge(2, 1),
			 Edge(3, 2), Edge(4, 5), Edge(5, 4)]

	# construct graph from given list of edges
	graph = Graph(edges)

	# print adjacency list representation of the graph
	graph.print()
                