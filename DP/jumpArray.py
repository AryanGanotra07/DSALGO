class Solution:
    # @param A : list of integers
    # @return an integer
    def canJump(self, a):
        
        # This variable denotes the maximum array elem we can jump
        # initially it is zero
        max_jump = 0
        for i in range(len(a)):
            # If this index not reachable than return 0
            if i > max_jump:
                return 0
            #update max jump
            max_jump = max(max_jump, i + a[i])
        return 1