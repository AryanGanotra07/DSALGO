class Solution:
    # @param A : list of integers
    # @return an integer
    def candy(self, A):
        n = len(A)
        candies = [1] * n
        for i in range(n-1):
            if A[i+1] > A[i]:
                candies[i+1] = candies[i] + 1
        for i in range(n-1, 0, -1):
            if A[i-1] > A[i] and candies[i-1] <= candies[i]:
                candies[i-1] = candies[i] + 1
        return sum(candies)

                
