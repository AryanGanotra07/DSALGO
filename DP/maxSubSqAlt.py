def maxSumSubseq(A):
 
    n = len(A)
 
    # base case
    if n == 1:
        return A[0]
 
    # create an auxiliary space to store solution of sub-problems
    lookup = [None] * n
 
    # lookup[i] stores the maximum sum possible till index i
 
    # trivial case
    lookup[0] = A[0]
    lookup[1] = max(A[0], A[1])
 
    # traverse list from index 2
    for i in range(2, n):
 
        # lookup[i] stores the maximum sum we get by
 
        # 1. excluding current element & take maximum sum till index i-1
        # 2. including current element A[i] and take maximum sum till index i-2
        lookup[i] = max(lookup[i - 1], lookup[i - 2] + A[i])
 
        # if current element is more than max sum till current element
        lookup[i] = max(lookup[i], A[i])
 
    # return maximum sum
    return lookup[n - 1]
 
 
if __name__ == '__main__':
 
    A = [1, 2, 9, 4, 5, 0, 4, 11, 6]
    print("Maximum sum is", maxSumSubseq(A))