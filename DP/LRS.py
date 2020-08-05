def LCSDP(x,y,m,n):
    T = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1] and i!=j:
                T[i][j] = 1 + T[i-1][j-1]
            else:
                T[i][j] = max(T[i-1][j], T[i][j-1])
    return T

def printLRS(x,m,t):
    i, j = m, m
    res = ""
    while (i > 0 and j > 0):
        if (x[i-1] == x[j-1] and i != j):
            res= x[i-1]+res
            i -=1 
            j-=1
        else:
            if t[i-1][j] > t[i][j-1]:
                i-=1
            else:
                j-=1
    return res




if __name__ == '__main__':
    a = "ATACTCGGA"
    t = LCSDP(a,a,len(a), len(a))
    print(printLRS(a,len(a),t))
