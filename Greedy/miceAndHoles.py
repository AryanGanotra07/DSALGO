class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def mice(self, A, B):
        A.sort()
        B.sort()
        n = len(A)
        c = [0]*n
        for i in range(n):
            c[i] = abs(A[i]-B[i])
        return max(c)