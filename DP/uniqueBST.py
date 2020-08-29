import sys
sys.setrecursionlimit(1500000)
lookup = {}
def solve(A):
    if not A:
        return 1
    if A in lookup:
        return lookup[A]
    cnt = 0
    for i in range(1, A+1):
        l = solve(i-1)
        r = solve(A-i)
        cnt += l*r
    lookup[A] = cnt
    return cnt
    
class Solution:
    # @param A : integer
    # @return an integer
    def numTrees(self, A):
        if A <=2:
            return A
        return solve(A)
