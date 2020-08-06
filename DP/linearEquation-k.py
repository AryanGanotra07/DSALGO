def solve(coeff, i, rhs):
    
    if rhs == 0:
        return 1
    if rhs < 0 or i < 0:
        return 0
    return solve(coeff, i-1, rhs) + solve(coeff, i, rhs-coeff[i])
     

if __name__ == '__main__':
 
    # k coefficients of given equation
    coeff = [1, 2, 3]
    k = len(coeff)
 
    rhs = 4
    print("Total number of solutions are", solve(coeff, k - 1, rhs))