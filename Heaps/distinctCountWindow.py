class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        result = []
        
        n = len(A)
        
        if B > n:
            return result
            
        i = 0
        j = B
        
        window = {}
        
        for k in A[i:B]:
            if not window.get(k):
                window[k] = 1
            else:
                window[k] += 1
                
        result.append(len(window))

        while j < n:
            
            if window.get(A[i]):
                if window[A[i]]:
                    window[A[i]] -= 1
                    
                    if not window[A[i]]:
                        del window[A[i]]
            
            if not window.get(A[j]):
                window[A[j]] = 1
            else:
                window[A[j]] += 1
            
            result.append(len(window))
            
            i += 1
            j += 1

        return result
            
            
            
            