def solve(i,A):
    if i >A:
        return 0
    if i==A:
        return 1
    return solve(i+1,A) + solve(i+2, A)
    
def solveDP(A):
    if A<=1:
        return 1
    t = [0]*(A+1)
    t[0] = 1
    t[1] = 1
    for i in range(2, A+1):
            t[i] = t[i-1] + t[i-2]
    return t[A]
    
    
    
class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        return solveDP( A)
