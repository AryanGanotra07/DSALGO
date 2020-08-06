def solve(a, m, n):
    if m ==0 or n==0:
        return float('inf')
    if m==1 and n==1:
        return a[0][0]
    return a[m-1][n-1]  + min(solve(a, m-1, n), solve(a, m, n-1))

def solveMemoized(a, m, n):
    pass
#lookup table for m, n

def solveDP(a, m, n):
    t = [[0 for j in range(n)] for i in range(m)]
   
    
    for i in range(0, m):
        for j in range(0, n):
            t[i][j] = a[i][j]
            if i ==0 and j > 0:
                t[i][j] += t[0][j-1]
            elif j==0 and i > 0:
                t[i][j] += t[i-1][0]
            else:
                t[i][j] += min(t[i-1][j], t[i][j-1])
    return t[m-1][n-1]


if __name__ == "__main__":
    cost = [
            [4, 7, 8, 6, 4],
            [6, 7, 3, 9, 2],
            [3, 8, 1, 2, 4],
            [7, 1, 7, 3, 7],
            [2, 9, 8, 9, 3]
        ]
    
    print("The minimum cost is", solveDP(cost, len(cost), len(cost[0])))