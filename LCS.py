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
    

if __name__ == '__main__':
    s1 = "abcdgh"
    s2 = "abedfhr"
    n = len(s1)
    m = len(s2)
    print(LCSMemoized(s1, s2, n, m))