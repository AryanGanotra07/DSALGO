class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return an integer
    def canCompleteCircuit(self, A, B):
        n = len(A)
        s = 0 
        d = 0
        start = 0
        for i in range(n):
            s+=A[i] - B[i]
            if s<0:
                start = i+1
                d+=s
                s = 0
        if s+d>=0:
            return start
        return -1
            
            
        
            
