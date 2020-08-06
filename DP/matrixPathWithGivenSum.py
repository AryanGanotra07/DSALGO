def solve(m, i, j, c):
    if c < 0:
        return 0
    if i == 0 and j==0:
        return 1 if m[0][0] == c else 0
    if i == 0:
        return solve(m, 0, j-1, c-m[i][j])
    if j==0:
        return solve(m, i-1, 0, c-m[i][j])
    return solve(m, i-1, j, c-m[i][j]) + solve(m  , i, j-1, c-m[i][j])

def solveMemoized(m, i, j, k):
    #find in lookup
    pass

if __name__ == '__main__':
 
    mat = [
        [4, 7, 1, 6],
        [5, 7, 3, 9],
        [3, 2, 1, 2],
        [7, 1, 6, 3]
    ]
 
    cost = 25
 
    print("Total paths with cost", cost, "are",
          solve(mat, len(mat) - 1, len(mat[0]) - 1, cost))