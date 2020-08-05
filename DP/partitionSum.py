def partitionSum(A, n):
    if (sum(A) %2!=0):
        return False
    s = sum(A)//2
    return partitionSumDP(A,n,s)

def partitionSumRecursion(A,n,s):
    if (s == 0):
        return True
    if (n < 0 or s < 0):
        return False
    include = partitionSumRecursion(A, n-1,s-A[n])
    if (include):
        return include
    exclude = partitionSumRecursion(A,n-1,s)
    return exclude

def partitionSumMemoized(A,n,s):
    if (s==0):
        return True
    if (n < 0 or s < 0):
        return False
    key = (n,s)
    if key in lookup:
        include = lookup[key]
        if (include):
            return True
    else:
        include = partitionSumMemoized(A, n-1,s-A[n])
        if include:
            lookup[key] = include
        else:
            exclude = partitionSumRecursion(A,n-1,s)
            lookup[key] = exclude
    return lookup[key]

def partitionSumDP(A,n,s):
    T = [[False for j in range(s+1)] for i in range(len(A)+1)]
    for i in range(len(A)+1):
        T[i][0] = True
    for i in range(1,len(A)+1):
        for j in range(1,s+1):
            if (A[i-1] > j):
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = T[i-1][j] or T[i-1][j-A[i-1]]
    return T[len(A)][s]


lookup = {}
if __name__ == '__main__':
    A = [3,1,1,2,2,1]
    print(partitionSum(A, len(A)-1))