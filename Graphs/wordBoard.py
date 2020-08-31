import sys
sys.setrecursionlimit(150000000)
def solve(A,i, j, m, n, B, k):
    if i >= m or j >= n or i < 0 or j < 0 or A[i][j]!=B[k]:
        return False
    if k == len(B)-1:
        return True
   
    
    a = solve(A, i+1, j, m, n, B, k+1)
    b = solve(A, i-1, j, m, n, B, k+1)
    c = solve(A, i, j+1, m, n, B, k+1)
    d = solve(A, i, j-1, m, n, B, k+1)

    if a or b or c or d:
        return True
    return False
def check(A, B):
    m = len(A)
    n = len(A[0])
    k = len(B)
    for i in range(m):
        for j in range(n):
            if A[i][j] == B[0]:
                if solve(A, i, j, m, n, B, 0):
                    return True
    return False
    
    
    
class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def exist(self, A, B):
        return 1 if check(A,B) else 0