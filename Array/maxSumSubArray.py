def maxSumSubArray(A):
    mx = float('-inf')
    mx_c = 0
    for i in range(len(A)):
        mx_c = max(A[i], mx_c + A[i])
        mx = max(mx_c, mx)
    return mx

print(maxSumSubArray( [-2, 1, -3, 4, -1, 2, 1, -5, 4]))