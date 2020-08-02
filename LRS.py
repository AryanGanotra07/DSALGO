def LCSDP(x,y,m,n):
    T = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1] and i!=j:
                T[i][j] = 1 + T[i-1][j-1]
            else:
                T[i][j] = max(T[i-1][j], T[i][j-1])
    return T[m][n]

if __name__ == '__main__':
    a = "ATACTCGGA"
    print(LCSDP(a,a,len(a), len(a)))
