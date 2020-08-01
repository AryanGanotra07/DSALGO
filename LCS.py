def LCSRecursive(s1, s2, n, m):
    if n == 0 or m == 0:
        return 0
    if s1[n-1] == s2[m-1]:
        return 1 + LCSRecursive(s1, s2, n-1, m-1)
    else:
        return max(LCSRecursive(s1, s2, n-1, m), LCSRecursive(s1, s2, n, m-1))
    

if __name__ == '__main__':
    s1 = "abcdgh"
    s2 = "abedfhr"
    n = len(s1)
    m = len(s2)
    print(LCSRecursive(s1, s2, n, m))