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
    return T

def printScs(x,y,m, n,t):
    i, j = m, n
    res = []
    while (i >  0 and j > 0):
        if x[i-1] == y[j-1]:
            res.append(x[i-1])
            i -= 1
            j -=1
        else:
            if (t[i-1][j] > t[i][j-1]):
                
                res.append(x[i-1])
                i -=1
            else:
                res.append(y[j-1])
             
                j-=1
    while (i > 0):
        res.append(x[i-1])
        i-=1
    while (j > 0):
        res.append(y[j-1])
        j-=1

    res.reverse()
    return res




if __name__ == '__main__':
    x = "abcdef"
    y = "abedgf"
    m = len(x)
    n = len(y)
    t = lcsRecursiveDP(x,y,m,n)
    print(t)
    print(printScs(x,y,m,n,t))
    # print(m+n-lcsRecursiveDP(x,y,m,n)) #scs
