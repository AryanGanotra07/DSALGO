def lbs(a):
    n = len(a)
    I = [0]*n
    D = [0]*n
    I[0] = 1
    for i in range(1, n):
        for j in range(i):
            if (a[i] > a[j] and I[i] < I[j]):
                I[i] = I[j]
        I[i]+=1
    D[n-1] = 1
    for i in reversed(range( n-1)):
        for j in range(n-1,i,-1):
            if (a[i]  > a[j] and D[i] < D[j]):
                D[i] = D[j]
        D[i]+=1
    lb = 1
    for i in range(n):
        lb = max(lb, I[i] + D[i] - 1)
    return lb

def LBS(A):
 
    n = len(A) - 1
 
    # I[i] stores the longest increasing subsequence ending with A[i]
    I = [[] for _ in range(n + 1)]
    I[0].append(A[0])
 
    for i in range(1, n + 1):
        for j in range(i):
            if len(I[i]) < len(I[j]) and A[i] > A[j]:
                I[i] = I[j].copy()
 
        I[i].append(A[i])
 
    # D[i] stores the longest decreasing subsequence starting from A[i]
    D = [[] for _ in range(n + 1)]
    D[n].insert(0, A[n])
 
    for i in reversed(range(n)):
        for j in reversed(range(i + 1, n + 1)):
            if len(D[i]) < len(D[j]) and A[i] > A[j]:
                D[i] = D[j].copy()
        D[i].insert(0, A[i])
 
    # find peak element index
    peak = 0
    for i in range(1, n + 1):
        if (len(I[i]) + len(D[i])) > (len(I[peak]) + len(D[peak])):
            peak = i
 
    print("Longest Bitonic Subsequence is: ", end='')
 
    # print longest increasing subsequence ending at peak element
    print(I[peak], end='')
 
    # pop front element of LDS as it points to same element as rear of LIS
    D[peak].pop(0)
 
    # print longest decreasing subsequence starting from peak element
    print(D[peak])
 
 
if __name__ == '__main__':
 
    A = [4, 2, 5, 9, 7, 6, 10, 3, 1]
    LBS(A)