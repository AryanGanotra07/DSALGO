

def coinChangeRecursionWrong(c, n):
    if n==0:
        return 1
    if n<0:
        return 0
    cnt = 0
    for i in range(len(c)):
        cnt += coinChangeRecursionWrong(c,n-c[i])
    return cnt

def count(S, n, N):
 
    # if total is 0, return 1 (solution found)
    if N == 0:
        return 1
 
    # return 0 (solution do not exist) if total become negative or
    # no elements are left
    if N < 0 or n < 0:
        return 0
 
    # Case 1. include current coin S[n] in solution and recur
    # with remaining change (N - S[n]) with same number of coins
    incl = count(S, n, N - S[n])
 
    # Case 2. exclude current coin S[n] from solution and recur
    # for remaining coins (n - 1)
    excl = count(S, n - 1, N)
 
    # return total ways by including or excluding current coin
    return incl + excl



def countMemoized(c, n, N):
    if N == 0:
        return 1
    if n < 0  or N < 0:
        return 0
    key = (n, N)
    if key not in lookup:
        incl = countMemoized(c, n, N-c[n])
        excl = countMemoized(c, n-1, N)
        lookup[key] = incl + excl
    return lookup[key]

def countDP(c, N):
    n = len(c)
    T = [[0 for j in range(N+1)] for i in range(n+1)]
    for i in range(n + 1):
        T[i][0] = 1
    for i in range(1, n+1):
        for j in range(1, N+1):
           
            if (c[i-1] > j):
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = T[i-1][j] + T[i][j-c[i-1]]
    return T[n][N]

    
 
lookup = {}    

if __name__ == '__main__':
    # n coins of given denominations
    S = [1, 2, 3]
 
    # Total Change required
    N = 4
 
    print("Total number of ways to get desired change is", countDP(S,  N))