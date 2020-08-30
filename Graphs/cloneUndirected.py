import sys
sys.setrecursionlimit(15000000)
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        visited = {}
        def clone(node, visited):
            if node not in visited:
                tmp = UndirectedGraphNode(node.label)
                visited[node] = tmp
                tmp.neighbors = [clone(n, visited) for n in node.neighbors]
                
            return visited[node]
        clone(node, visited)
        return visited[node]
        
