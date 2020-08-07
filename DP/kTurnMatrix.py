def valid(m,n, i, j):
    if i >= 0 and i < m and j >=0 and j<n:
        return True
    return False
def solve(k,m,n ,isCol, i= 0, j=0 ):
    if k==-1 or not valid(m,n,i,j):
        return 0
    if k==0:
        if i== m-1 and j == n-1:
            return 1
        return 0
    if isCol:
        return solve(k, m, n, isCol, i+1, j ) + solve(k-1, m, n, not isCol, i, j+1)
    return solve(k, m, n, isCol, i, j+1 ) + solve(k-1, m, n, not isCol, i+1, j)

if __name__ == '__main__':
 
    # M x N matrix
    M = N = 3
 
    k = 4
    print("Total number of ways is", solve(k, M, N, True) + solve(k,M, N, False))
