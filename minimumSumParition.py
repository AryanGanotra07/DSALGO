def minSumPartitionDP(A):
    res = subsetSumDP(A,sum(A))
    mn = float('inf')
    for r in res:
        mn = min(mn, sum(A)-2*r)
    return mn



def subsetSumDP(A, s):
    T = [[False for j in range(s+1)] for i in range(len(A)+1)]
    for i in range(len(A)+1):
        T[i][0] = True
    
    for i in range(1, len(A)+1):
        for j in range(1, s+1):
            if (A[i-1] > j):
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = T[i-1][j] or T[i-1][j-A[i-1]]
    result = []
    for j in range((s+1)//2):
        if (T[len(A)][j] == True):
            result.append(j)
    return result

def minSumPartitionRecursion(A, n, s1 = 0, s2 = 0):
    if n < 0:
        return abs(s1-s2)
    
    inc = minSumPartitionRecursion(A, n-1, s1 + A[n], s2)
    exc = minSumPartitionRecursion(A, n-1, s1, s2 + A[n])

    return min(inc, exc)


def minSumPartitionMemoized(A, n, s1=0, s2=0):
    if n<0:
        return abs(s1-s2)
    
    key = (n,s1,s2)
    if key not in lookup:
        inc = minSumPartitionRecursion(A, n-1, s1 + A[n], s2)
        exc = minSumPartitionRecursion(A, n-1, s1, s2 + A[n])
        lookup[key]= min(inc, exc)
    return lookup[key]



lookup = {}

def minSumPartitionDPAnother(A):
    pass




if __name__ == '__main__':
    A= [10,20,15,5,25]
    print(minSumPartitionMemoized(A, len(A)-1 ))
