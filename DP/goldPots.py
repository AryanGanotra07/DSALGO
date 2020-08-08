def solve(a, i, j):
    if i == j:
        return a[i]
    if i+1==j:
        return max(a[i], a[j])
    s = a[i] + min(solve(a, i+2, j), solve(a, i+1, j-1))
    e = a[j] + min(solve(a, i+1, j-1), solve(a, i, j-2))
    return max(s,e)

#prepare a lookup table

def calculate(T, i, j):
    return T[i][j] if i <= j else 0
 
 
def optimalStrategy(coin):
 
    n = len(coin)
 
    # base case: one pot left, only one choice possible
    if n == 1:
        return coin[0]
 
    # if we're left with only two pots, choose one with maximum coins
    if n == 2:
        return max(coin[0], coin[1])
 
    # create a dynamic 2D matrix to store sub-problem solutions
    T = [[0 for x in range(n)] for y in range(n)]
 
    for iteration in range(n):
        i = 0
        j = iteration
        while j < n:
            start = coin[i] + min(calculate(T, i + 2, j), calculate(T, i + 1, j - 1))
            end = coin[j] + min(calculate(T, i + 1, j - 1), calculate(T, i, j - 2))
            T[i][j] = max(start, end)
            i = i + 1
            j = j + 1
 
    return T[0][n - 1]


if __name__ == '__main__':
 
    # pots of gold (even number) arranged in a line
    coin = [4, 6, 2, 3]
 
    print("Maximum coins collected by player is", 
          solve(coin, 0, len(coin) - 1))
