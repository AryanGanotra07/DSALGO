def LCSDP(x,y,m, n):
    T = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if (x[i-1] == y[j-1]):
                T[i][j] = 1+ T[i-1][j-1]
            else:
                T[i][j] = max (T[i-1][j], T[i][j-1])
    return T

def printLCS(x,y,m,n, t):
    i, j = m, n
    res = []
    while (i > 0 and j > 0):
        if x[i-1] == y[j-1]:
            res.append(x[i-1])
            i-=1
            j-=1
        else:
            if t[i-1][j] > t[i][j-1]:
                i -=1
            else:
                j -=1 
    res.reverse()
    return ''.join(res)
            




if __name__ == "__main__":
    x =  "ABBDCACB"
    m = len(x)
    lx = list(x)
    lx.reverse()
    # print(lx)
    y = ''.join(lx)
    # print(y)
    n = len(y)
    t = LCSDP(x,y,m,n)
    print(printLCS(x,y,m,n,t))

