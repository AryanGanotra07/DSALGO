def MSISDP(a):
    n = len(a)
    t = [0] * n
    t[0] = a[0]
    for i in range(1,n):
        for j in range(i):
            if a[i] > a[j] and t[i] < t[j]:
                t[i] = t[j]
        t[i]+=a[i]
    return max(t)

def printLIS(A):
    LIS = [[] for _ in range(len(A))]
 
    # LIS[0] denotes longest not increasing subsequence ending with A[0]
    LIS[0].append(A[0])
    sum = [0] * len(A)
    sum[0] = A[0]
 
    # start from second element in the list
    for i in range(1, len(A)):
 
        # do for each element in sublist[0..i-1]
        for j in range(i):
 
            # find longest increasing subsequence that ends with A[j]
            # where A[j] is less than the current element A[i]
 
            if A[j] < A[i] and len(LIS[j]) > len(LIS[i]):
                LIS[i] = LIS[j].copy()
                sum[i] = sum[j]    
 
        # include A[i] in LIS[i]
        LIS[i].append(A[i])
        sum[i] += A[i]
 
    # j will contain index of LIS
    j = 0
    for i in range(1, len(A)):
        if sum[i] > sum[j]:
            j = i
 
 
 
    # print LIS
    print(LIS[j])

if __name__ == '__main__':
 
    A = [8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11]
    print("Maximum sum of increasing subsequence is",
          printLIS(A))
 