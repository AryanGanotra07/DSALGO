class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        if len(A) == 0 or len(A) ==1:
            return 0
        profits = [0]*len(A)
        max_price = A[len(A)-1]
        n = len(A)
        for i in range(n-2, -1, -1):
            if A[i] > max_price:
                max_price = A[i]
            profits[i] = max(profits[i+1], max_price - A[i])
            
        min_price = A[0]
        for i in range(1, n):
            if A[i] < min_price:
                min_price = A[i]
            profits[i] = max(profits[i-1], profits[i] + A[i] - min_price)
        return profits[n-1]
        
