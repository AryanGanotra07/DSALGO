class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        if A < B:
            A, B = B, A
        return A%B + C - 1