def LCSRecursive(x, y, z, m, n, o):
    if m==0 or n==0 or o==0:
        return 0
    if x[m-1] == y[n-1] == z[o-1]:
        return 1 + LCSRecursive(x,y,z,m-1, n-1, o-1)
    
    return max(LCSRecursive(x,y,z,m-1, n, o), LCSRecursive(x,y,z,m,n-1,o), LCSRecursive(x,y,z,m,n,o-1))

def LCSMemoized(x,y,z, m, n, o):
    if m==0 or n==0 or o==0:
        return 0
    key = (m,n,o)
    if key not in lookup:
        if x[m-1] == y[n-1] == z[o-1]:
            lookup[key] = 1 + LCSRecursive(x,y,z,m-1, n-1, o-1)
    
        lookup[key] = max(LCSRecursive(x,y,z,m-1, n, o), LCSRecursive(x,y,z,m,n-1,o), LCSRecursive(x,y,z,m,n,o-1))

lookup = {}

def LCSDP(x, y ,z, m, n, o):
    T =[[[0 for k in range(o+1)]for j in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            for k in range(o+1):
                if x[i-1] == y[j-1] == z[k-1]:
                    T[i][j][k] = 1 + T[i-1][j-1][k-1]
                else:
                    T[i][j][k] = max(T[i-1][j][k], T[i][j-1][k], T[i][j][k-1])
    return T[m][n][o]


if __name__ == '__main__':
    s1 = "abcdgh"
    s2 = "abedfhr"
    s3 = "abc"
    m = len(s1)
    n = len(s2)
    o = len(s3)
    print(LCSRecursive(s1, s2, s3, m,n,o))