def subsetSumRecursion(A,n, s):
    if s == 0:
        return True
    if n < 0 or s < 0:
        return False
    include = subsetSumRecursion(A, n-1, s - A[n])
    if include:
        return True
    exclude = subsetSumRecursion(A,n-1,s)
    return exclude

def subsetSumMemoized(A,n,s):
    if (s==0):
        return True
    if n < 0 or s < 0:
        return False
    key = (n,s)
    if key in lookup:
        return lookup[key]
    include = subsetSumMemoized(A,n-1,s-A[n])
    exclude = subsetSumMemoized(A,n-1,s)
    if include or exclude:
        lookup[key] = True
    else:
        lookup[key] = False
    return lookup[key]

def subsetSumDP(A,s):
    T = [[False for j in range(s+1)] for i in range(len(A)+1)]
    for i in range(len(A)+1):
        T[i][0] = True
    for i in range(1,len(A)+1):
        for j in range(1, s+1):
            if (A[i-1] > j):
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = T[i-1][j] or T[i-1][j-A[i-1]]
    return T[len(A)][s]



lookup = {}

if __name__ == '__main__':
    A = [7,3,2,5,8]
    s = 14
    print(subsetSumDP(A,  s))