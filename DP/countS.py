def count(x,y, m, n):
    if m < n:
        return 0
    if m == 1 and n==1:
        return 1 if x[m-1] == y[n-1] else 0
    if n==0:
        return 1
    if m == 0:
        return 0
    return (count(x,y,m-1,n-1) if x[m-1] == y[n-1] else 0) + count(x,y,m-1,n)

def countDP(x,y, m,n):
    t = [[0 for j in range(n+1)] for i in range(m+1)]
    for j in range(m+1):
        t[j][0] = 1
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1] == y[j-1]:
                t[i][j] = t[i-1][j-1] + t[i-1][j] 
            else:
                t[i][j] = t[i-1][j]
    return t[m][n]




if __name__ == '__main__':
 
    X = "subsequence"   # Input String
    Y = "sue"           # Pattern
 
    print(countDP(X, Y, len(X), len(Y)))