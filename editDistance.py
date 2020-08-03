def editDistanceecursive(x,m,y,n):
    if m == 0 :
        return n
    if n == 0:
        return m
    if x[m-1] == y[n-1]:
        return editDistanceecursive(x,m-1, y, n-1)
    return min(editDistanceecursive(x,m-1, y, n) + 1, editDistanceecursive(x,m-1,y, n-1) + 1, editDistanceecursive(x, m, y, n-1) + 1)

if __name__ == '__main__':
 
    X = "kitten"
    Y = "sitting"
 
    print("The Levenshtein Distance is", editDistanceecursive(X, len(X), Y, len(Y)))