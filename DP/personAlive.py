def aliveProbability(x, y, n, dp):
 
    # base case
    if n == 0:
        return 1.0
 
    # calculate unique dict key from current coordinates(x, y) of person
    # and number of steps(n) left
    key = (x, y, n)
 
    # if sub-problem is seen for the first time
    if key not in dp:
 
        p = 0.0
 
        # move one step up
        if x > 0:
            p += 0.25 * aliveProbability(x - 1, y, n - 1, dp)
 
        # move one step down
        if x < N - 1:
            p += 0.25 * aliveProbability(x + 1, y, n - 1, dp)
 
        # move one step left
        if y > 0:
            p += 0.25 * aliveProbability(x, y - 1, n - 1, dp)
 
        # move one step right
        if y < N - 1:
            p += 0.25 * aliveProbability(x, y + 1, n - 1, dp)
 
        dp[key] = p
 
    return dp[key]
 
 
if __name__ == '__main__':
 
    N = 3
 
    n = 3            # number of steps to be taken
    x = y = 0        # starting coordinates
 
    # dict to store solution to already computed subproblems
    dp = {}
 
    # calculate alive Probability
    print("Alive probability is", aliveProbability(x, y, n, dp))