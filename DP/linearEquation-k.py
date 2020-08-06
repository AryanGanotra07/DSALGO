def solve(coeff, i, rhs):
    
    if rhs == 0:
        return 1
    if rhs < 0 or i < 0:
        return 0
    return solve(coeff, i-1, rhs) + solve(coeff, i, rhs-coeff[i])

def solveMem(coeff, i, rhs):
    #store i, rhs in lookup 
    pass

def solveDP(coeff, rhs):
 
    k = len(coeff)
 
    T = [[0] * (rhs + 1) for _ in range(k + 1)]
 
    for i in range(k + 1):
        T[i][0] = 1
 
    for i in range(1, k + 1):
        for j in range(1, rhs + 1):
            if coeff[i - 1] > j:
                T[i][j] = T[i - 1][j]
            else:
                T[i][j] = T[i - 1][j] + T[i][j - coeff[i - 1]]
 
    return T[k][rhs]
     

if __name__ == '__main__':
 
    # k coefficients of given equation
    coeff = [1, 2, 3]
    k = len(coeff)
 
    rhs = 4
    print("Total number of solutions are", solve(coeff, k - 1, rhs))