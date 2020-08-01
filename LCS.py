def LCSRecursive(s1, s2, n, m):
    if n == 0 or m == 0:
        return 0
    if s1[n-1] == s2[m-1]:
        return 1 + LCSRecursive(s1, s2, n-1, m-1)
    else:
        return max(LCSRecursive(s1, s2, n-1, m), LCSRecursive(s1, s2, n, m-1))


def LCSMemoized(s1, s2, n, m):
    if n==0 or m==0:
        return 0
    key = (n, m)
    if key not in lookup:
        if s1[n-1] == s2[m-1]:
            lookup[key] = 1 + LCSMemoized(s1, s2, n-1, m-1)
        else:
            lookup[key] = max(LCSMemoized(s1, s2, n-1, m), LCSMemoized(s1, s2, n, m-1))
    return lookup[key]
lookup = {}

def LCSDP(s1, s2, n, m):
    T = [[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if (s1[i-1] == s2[j-1]):
                T[i][j] = 1 + T[i-1][j-1]
            else:
                T [i][j] = max(T[i-1][j], T[i][j-1])
    return T[n][m]
     

if __name__ == '__main__':
    s1 = "abcdgh"
    s2 = "abedfhr"
    n = len(s1)
    m = len(s2)
    print(LCSDP(s1, s2, n, m))