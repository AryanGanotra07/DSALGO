def minCoinChangeRecursive(s, N):
    if (N==0):
        return 0
    if N < 0:
        return float('inf')
    coins = float('inf')
    for i in range(len(S)):
        incl = minCoinChangeRecursive(s, N-s[i])
        if incl != float('inf'):
            coins = min(coins, incl+1)
    
    return coins

def minCoinChangeMemoized(S, N):
    if N==0:
        return 0 
    if N < 0:
        return float('inf')
    coins = float('inf')
    for i in range(len(S)):
        key = (i,N)
        if key not in lookup:
            incl = minCoinChangeMemoized(S, N-S[i])
            if incl != float('inf'):
                coins = min(coins, incl + 1)
            lookup[key] = coins
        else:
            coins = lookup[key]
    return coins
        

lookup = {}

def minCoinChangeDP(S, N):
    T = [[float('inf') for j in range(N+1)] for i in range(len(S) + 1)]
    for i in range(len(S)+1):
        T[i][0] = 0
    for i in range(1,len(S)+1):
        for j in range(1, N+1):
            if (S[i-1] > j):
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = min(T[i-1][j], T[i][j-S[i-1]]+1)
    return T[len(S)][N]

    

if __name__=='__main__':
    S = [1,3,5,7]
    N = 15
    print(minCoinChangeDP(S, N))