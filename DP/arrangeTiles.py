def totalWays(n):
 
    # base cases
    if n < 1:
        return 0
 
    if n < 4:
        return 1
 
    if n == 4:
        return 2
 
    # combine results of placing a tile horizontally and placing 4 tiles vertically
    return totalWays(n - 1) + totalWays(n - 4)

def arrangeDP(n):
    if n < 1:
        return 0
    if n<4:
        return 1
    t = [0 for i in range(n+1)]
    t[1] = t[2] = t[3] = 1
    t[4] = 2
    for i in range(5, n+1):
        t[i] = t[i-1] + t[i-4]
    return t[n]

 
 
if __name__ == '__main__':
 
    n = 5
    print("Total number of ways are", arrangeDP(n))