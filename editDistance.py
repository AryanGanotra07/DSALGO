def editDistanceecursive(x,m,y,n):
    if m == 0 :
        return n
    if n == 0:
        return m
    if x[m-1] == y[n-1]:
        return editDistanceecursive(x,m-1, y, n-1)
    return min(editDistanceecursive(x,m-1, y, n) + 1, editDistanceecursive(x,m-1,y, n-1) + 1, editDistanceecursive(x, m, y, n-1) + 1)

def editDistanceDp(x, m, y, n):
    t = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(1, m+1):
        t[i][0] = 1
    for j in range(1, n+1):
        t[0][j] = 1
    # print(t)
    for i in range(1, m+1):
        for j in range(1,n+1):
            if x[i-1] == y[j-1]:
                t[i][j] = t[i-1][j-1]
            else:
                t[i][j] = min(t[i-1][j-1] +1 , t[i-1][j] + 1, t[i][j-1] + 1)
    # print(t)
    return t[m][n]

if __name__ == '__main__':
 
    X = "kitten"
    Y = "sitting"
 
    print("The Levenshtein Distance is", editDistanceDp(X, len(X), Y, len(Y)))