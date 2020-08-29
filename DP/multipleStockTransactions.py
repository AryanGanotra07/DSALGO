class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        maxprofit=0
        for i in range(1,len(A)):
            if A[i]>A[i-1]:
                maxprofit +=A[i]-A[i-1]
        return maxprofit
