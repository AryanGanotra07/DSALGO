def isNotSafe(mat, i, j):
    return i < 0 or i >= len(mat) or j < 0 or j >= len(mat[0]) or mat[i][j] == -1
def solve(m, i, j):
    if isNotSafe(m, i, j):
        return 0 
    if m[i][j]!= -1:
        return m[i][j] + max(solve(m, i, j-1), solve(m, i+1,j)) if i % 2 != 0 else m[i][j] + max(solve(m, i, j+1), solve(m, i+1,j))
    return 0

def findMaximum(mat):
 
    # M x N matrix
    (M, N) = (len(mat), len(mat[0]))
 
    # T[i][j] stores maximum value that can be collected
    # from any cell to cell (i-1, j-1)
    T = [[0 for x in range(N + 1)] for y in range(M + 1)]
 
    # process each row one by one and fill lookup table T
    for i in range(1, M + 1):
 
        # handle odd and even row separately
        if i & 1:
            # process current row from left to right
            for j in range(1, N + 1):
                if mat[i - 1][j - 1] != -1:
                    T[i][j] = mat[i - 1][j - 1] + max(T[i][j - 1], T[i - 1][j])
 
        else:
            # process current row from right to left
            for j in range(N - 1, 0, -1):
                if mat[i - 1][j - 1] != -1:
                    T[i][j] = mat[i - 1][j - 1] + max(T[i][j + 1], T[i - 1][j])
 
    # trace maximum ones starting from first cell
    i = j = 1
    res = T[i][j]
 
    while i <= M and 0 <= j <= N:
        if T[i][j] == T[i + 1][j] or T[i][j] + 1 == T[i + 1][j]:
            i = i + 1
        elif T[i][j] == T[i][j + 1] or T[i][j] + 1 == T[i][j + 1]:
            j = j + 1
        elif T[i][j] == T[i][j - 1] or T[i][j] + 1 == T[i][j - 1]:
            j = j - 1
        else:
            break
 
        res = T[i][j]
 
    return res

if __name__ == '__main__':
 
    mat = [
        [1, 1, -1, 1, 1],
        [1, 0, 0, -1, 1],
        [1, 1, 1, 1, -1],
        [-1, -1, 1, 1, 1],
        [1, 1, -1, -1, 1]
    ]
 
    print("Maximum value collected is", findMaximum(mat))