class Edge:
    def __init__(self,src, dest):
        self.src = src
        self.dest = dest

class Graph:
    def __init__(self, edges):
        self.adj = [[]for i in range(len(edges))]
        for edge in edges:
            self.adj[edge.src].append(edge.dest)
    def print(self):
        for src in range(len(self.adj)):
            for dest in self.adj[src]:
                print(f"({src} -> {dest})", end = " ")
            print()
    def countDependencies(self):
        sm = 0
        for src in range(len(self.adj)):
                sm+=len(self.adj[src])
        return sm


if __name__ == '__main__':

	# Input: Edges in a directed graph
    edges = [Edge(0, 2), Edge(0, 3), Edge(1, 3), Edge(2, 3)]

    # construct graph from given list of edges
    graph = Graph(edges)

    graph.print()
    print(graph.countDependencies())