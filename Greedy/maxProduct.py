class Solution:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
        A.sort()
        a = A[0]*A[1]*A[-1]
        
        b = A[-1]*A[-2]*A[-3]
        return max(a,b)
