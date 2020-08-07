def totalWays(n):
 
    if n <= 1:
        return 1
 
    # base case: 1 way (with no steps)
    a = 1
 
    # There is only 1 way to reach the 1st stair
    b = 1
 
    # There are 2 ways to reach the 2nd stair
    c = 2
 
    for i in range(3, n + 1):
        result = a + b + c
 
        a = b
        b = c
        c = result
 
    return c
 
 
if __name__ == '__main__':
 
    n = 4
    print(f"Total ways to reach the {n}'th stair are {totalWays(n)}")