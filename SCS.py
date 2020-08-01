def lcsRecursive(x,y,m,n):
    if m==0 or n==0:
        return 0
    if x[m-1] == y[n-1]:
        return 1 + lcsRecursive(x,y,m-1, n-1)
    return max(lcsRecursive(x,y,m-1,n), lcsRecursive(x,y,m, n-1))

def lcsRecursiveDP(x,y, m, n):
    T = [[0 for j in range(n+1)]for i in range(m+1)]
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1] == y[j-1]:
                T[i][j] = 1 + T[i-1][j-1]
            else:
                T[i][j] = max(T[i-1][j], T[i][j-1])
    return T[m][n]


if __name__ == '__main__':
    x = "abcdef"
    y = "abedgf"
    m = len(x)
    n = len(y)
    print(m+n-lcsRecursiveDP(x,y,m,n)) #scs
