class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        c = min(A-1,B-1)
        c += min(8-A, B-1)
        c+= min(8-A, 8-B)
        c+= min(A-1, 8-B)
        return c