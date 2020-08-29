def solve(A):
    profit = 0
    cp = float('inf')
    for i in range(len(A)):
        cp = min(cp, A[i])
        profit = max(profit, A[i] - cp)
    return profit
            
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        if len(A) == 0:
            return 0
        if len(A) == 1:
            return 0
        return solve(A)
            
