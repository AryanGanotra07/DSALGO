def totalWays(n, m):
 
    # create a list of n+1 size for storing solutions to the sub-problems
    lookup = [None] * (n + 1)
 
    # base case: 1 way (with no steps)
    lookup[0] = 1
 
    # 1 way to reach the 1st stair
    lookup[1] = 1
 
    # 2 ways to reach the 2nd stair
    lookup[2] = 2
 
    # Fill the lookup table in bottom-up manner
    for i in range(3, n + 1):
        lookup[i] = 0
        j = 1
        while j <= m and (i - j) >= 0:
            lookup[i] += lookup[i - j]
            j = j + 1
 
    return lookup[n]
 
 
if __name__ == '__main__':
 
    n = 4
    m = 3
 
    print(f"Total ways to reach the {n}'th stair with at-most {m} steps are",
                            totalWays(n, m))