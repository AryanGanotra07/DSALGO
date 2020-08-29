import sys
sys.setrecursionlimit(1500000)
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, A):
        if len(A) == 1:
            return A[0]
        max_ending = min_ending = 0
        max_so_far = 0
        for i in A:
            temp = max_ending
            max_ending = max(i, i*max_ending, i*min_ending)
            min_ending = min(i, i*temp, i*min_ending)
            max_so_far = max(max_so_far, max_ending)
        return max_so_far
