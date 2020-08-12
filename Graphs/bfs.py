from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def bfs(self, u):
        visited = [False]* len(self.graph)
        q = []
        q.append(u)
        while q:
            elem = q.pop(0)
            visited[elem] = True
            print(elem, end = " ")
            for v in self.graph[elem]:
                if visited[v] == False:
                    q.append(v)
    def __dfsutile(self, u, visited):
        print(u, end = " ")
        visited[u] = True
        for v in self.graph[u]:
            if visited[v] == False:
                self.__dfsutile(v, visited)
    def dfs(self, u):
        visited = [False] * len(self.graph)
        for u in self.graph:
            if visited[u] == False:
                self.__dfsutile(u, visited)

g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
print ("Following is Depth First Traversal"
                  " (starting from vertex 2)") 
# g.bfs(2) 
g.dfs(2)
