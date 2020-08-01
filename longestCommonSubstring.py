
def LCSDP(s1, s2, n, m):
    T = [[0 for j in range(m+1)] for i in range(n+1)]
    result = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if (s1[i-1] == s2[j-1]):
                T[i][j] = 1 + T[i-1][j-1]
                result = max(result, T[i][j])
            else:
                T [i][j] = 0
    return result

def LCSRecursive(s1, s2, n, m, count = 0):
    if n == 0 or m == 0:
        return count
    if s1[n-1] == s2[m-1]:
        count = LCSRecursive(s1, s2, n-1, m-1, count + 1)
    return max(count, max(LCSRecursive(s1, s2, n-1,m, 0), LCSRecursive(s1, s2, n, m-1, 0)))
        
    


if __name__ == '__main__':
    a = "abc"
    b = "baba"
    print(LCSRecursive(a,b, len(a), len(b)))
    pass