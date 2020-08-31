import sys
sys.setrecursionlimit(150000000)
def dfs(A, i, j,m,n, visited):
    if i < 0 or j < 0 or i >= m or j >= n:
        return 
    if visited[i][j] == 1:
        return
    if A[i][j] != "X":
        return
    visited[i][j] = 1
    dfs(A,i+1, j,m,n ,visited)
    dfs(A, i-1,j,m,n ,visited)
    dfs(A, i, j+1,m,n ,visited)
    dfs(A, i, j-1,m,n, visited)
    
class Solution:
    # @param A : list of strings
    # @return an integer
    def black(self, A):
        
        m = len(A)
        n = len(A[0])
        visited = [[0 for j in range(n)]for i in range(m)]
        cnt =0
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 0 and A[i][j] == "X":
                    dfs(A, i, j,m,n, visited)
                    cnt += 1
        return cnt
                    
