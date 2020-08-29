def solve(A,n):
    if(n<=1):
        return 0
    if(A[0]==0):
        return -1
    md = A[0]
    step = A[0]
    cnt = 1
    for i in range(1, n):
        if i == n-1:
            return cnt
        md = max(md, i+A[i])
        step-=1
        if step ==0 :
            cnt+=1
            if i >=md:
                return -1
            else:
                step = md - i
    return -1
class Solution:
    # @param A : list of integers
    # @return an integer
    def jump(self, A):
        return solve(A, len(A))
