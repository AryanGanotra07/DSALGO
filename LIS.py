def LISRecursive(a,s, n, prev):
    if s == n:
        return 0
    excl = LISRecursive(a, s+1, n, prev)
    incl = 0
    if prev < a[s]:
        incl = LISRecursive(a, s+1, n, a[s]) + 1
    return max(incl, excl)

def LISMemoized(a, s, n, prev):
    if s == n:
        return 0
    key = (s, prev)
    if key not in lookup:
        excl = LISRecursive(a, s+1, n, prev)
        incl = 0
        if prev < a[s]:
            incl = LISRecursive(a, s+1, n, a[s]) + 1
        lookup[key] = max(incl, excl)
    return lookup[key]

def LISDP(a):
    n = len(a)
    t = [0] * n
    t[0] = 1
    for i in range(1,n):
        for j in range(i):
            if a[i] > a[j] and t[i] < t[j]:
                t[i] = t[j]
        t[i]+=1
    return max(t)

def printLIS(A):
    LIS = [[] for _ in range(len(A))]
 
    # LIS[0] denotes longest not increasing subsequence ending with A[0]
    LIS[0].append(A[0])
 
    # start from second element in the list
    for i in range(1, len(A)):
 
        # do for each element in sublist[0..i-1]
        for j in range(i):
 
            # find longest increasing subsequence that ends with A[j]
            # where A[j] is less than the current element A[i]
 
            if A[j] < A[i] and len(LIS[j]) > len(LIS[i]):
                LIS[i] = LIS[j].copy()
 
        # include A[i] in LIS[i]
        LIS[i].append(A[i])
 
    # j will contain index of LIS
    j = 0
    for i in range(len(A)):
        if len(LIS[j]) < len(LIS[i]):
            j = i
 
    # print LIS
    print(LIS[j])


lookup = {}
if __name__ == '__main__':
 
    A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
 
    print("Length of LIS is", LISDP(A))
    printLIS(A)
    