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

def printStrings(n, out="", last_digit=0):
 
    # if number becomes N-digit, print it
    if n == 0:
        print(out, end=' ')
        return
 
    # append 0 to the result and recur with one less digit
    printStrings(n - 1, out + '0', 0)
 
    # append 1 to the result and recur with one less digit
    # only if last digit is 0
    if last_digit == 0:
        printStrings(n - 1, out + '1', 1)

if __name__ == "__main__":
    n  = 5
    print(printStrings(5))