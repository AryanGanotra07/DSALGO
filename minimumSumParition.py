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



if __name__ == '__main__':
    A= [10,20,15,5,25]
    print(minSumPartitionDP(A))
