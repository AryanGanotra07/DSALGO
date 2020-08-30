class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        n = len(A)
        ans = A[0]
        count = 0
        for i in range(len(A)):
            if count == 0:
                ans = A[i]
            if A[i] == ans:
                count= count + 1
            else:
                count -= 1
                 
        return ans
            
