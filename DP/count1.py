def countRecursive(M, m, n, ms):
    if m==0 or n==0:
        return M[m][n], max(ms, M[m][n])
    left, ms = countRecursive(M, m,n-1, ms)
    top, ms = countRecursive(M, m-1, n, ms)
    topLef, ms = countRecursive(M, m-1,n-1, ms)
    size = 1 + min(left, top, topLef) if M[m][n] else 0
    return size, max(ms,size)


def countDP(M,m,n):
    T = [[0 for j in range(n+1)] for i in range(m+1)]
    mx = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if (M[i-1][j-1] == 1):
                T[i][j] = 1 + min(T[i-1][j], T[i-1][j-1], T[i][j-1])
            mx = max(mx, T[i][j])
    return mx


if __name__ == '__main__':
 
    M = [
        [0, 0, 1, 0, 1, 1],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1]
    ]
 
    # size stores the size of largest square sub-matrix of 1's
    #maxsize = countRecursive(M, len(M) - 1, len(M[0]) - 1, 0)[1]
    maxsize = countDP(M, len(M), len(M[0]))
 
    print("The size of largest square sub-matrix of 1's is", maxsize)