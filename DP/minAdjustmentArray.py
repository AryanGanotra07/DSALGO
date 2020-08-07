# Find minimum adjustment cost of a list
def minimalAdjustmentCost(A, target):
 
    # T[i][j] stores minimal adjustment cost on changing A[i] to j
    T = [[0 for x in range(M + 1)] for y in range(len(A))]
 
    # do for each element of the list
    for i in range(len(A)):
 
        # replace A[i] to j and calculate minimal adjustment cost T[i][j]
        for j in range(M + 1):
 
            # separately handle first element of list
            if i == 0:
                T[i][j] = abs(j - A[i])
            else:
                # initialize minimal adjustment cost to float('inf')
                T[i][j] = float('inf')
 
                # consider all k such that k >= max(j - target, 0) and
                # k <= min(M, j + target) and take minimum
                for k in range(max(j - target, 0), min(M, j + target) + 1):
                    T[i][j] = min(T[i][j], T[i - 1][k] + abs(A[i] - j))
 
    # return minimum value from last row of T table
    result = float('inf')
    for j in range(M + 1):
        result = min(result, T[-1][j])
 
    return result
 
 
if __name__ == '__main__':
 
    A = [55, 77, 52, 61, 39, 6, 25, 60, 49, 47]
    target = 10
 
    M = 100
 
    print("The minimal adjustment cost is", minimalAdjustmentCost(A, target))
 