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


lookup = {}
if __name__ == '__main__':
 
    A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
 
    print("Length of LIS is", LISDP(A))
    