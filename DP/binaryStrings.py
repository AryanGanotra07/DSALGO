def solve(n, ld):
    if n==0:
        return 0
    if n==1:
        return 1 if ld == 1 else 2
    if ld == 0:
        return solve(n-1, 1) + solve(n-1, 0)
    return solve(n-1, 0)

def solveDP(n):
    t=[[0 for x in range(2)]for i in range(n+1)]
    t[1][0] = 2
    t[1][1] = 1
    for i in range(2, n+1):
        t[i][0] = t[i-1][0]  + t[i-1][1]
        t[i][1] = t[i-1][0]
    return t[n][0]


if __name__ == "__main__":
    n  = 5
    print(solveDP(5))