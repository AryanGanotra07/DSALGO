def findLongestPath(M, i, j):
    if not isValid(M, i, j):
        return None
    path = None
    if i > 0 and M[i - 1][j] - M[i][j] == 1:
        path = findLongestPath(M, i - 1, j)
    if j + 1 < len(M) and M[i][j + 1] - M[i][j] == 1:
        path = findLongestPath(M, i, j + 1)
    if i + 1 < len(M) and M[i + 1][j] - M[i][j] == 1:
        path = findLongestPath(M, i + 1, j)
    if j > 0 and M[i][j - 1] - M[i][j] == 1:
        path = findLongestPath(M, i, j - 1)
    return f"{M[i][j]} - {path}" if path else f"{M[i][j]}"
    
def isValid(M, i, j):
    return 0 <= i < len(M) and 0 <= j < len(M)

def findLongestPathMemoized(M, i, j):
    pass
#store i,j in lookup hash. 

if __name__ == '__main__':
 
    M = [
        [10, 13, 14, 21, 23],
        [11, 9, 22, 2, 3],
        [12, 8, 1, 5, 4],
        [15, 24, 7, 6, 20],
        [16, 17, 18, 19, 25]
    ]
 
    res = None                 
    resSize = float('-inf')     
 
    # from each cell (i, j), find the longest path starting from it
    for i in range(len(M)):
        for j in range(len(M)):
 
            # str would be like 1 - 2 - 3 - 4 - 5 -
            str = findLongestPath(M, i, j)
 
            # find number of elements involved in current path
            size = str.count('-')
 
            # update result if longer path is found
            if size > resSize:
                res = str
                resSize = size
 
    # print the path
    print(res)