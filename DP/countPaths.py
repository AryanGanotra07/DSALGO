
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
# Bottom-up function to count all paths from the first cell (0,0)
# to the last cell (M-1,N-1) in a given M x N rectangular grid
def countPaths(m, n):
 
    # T[i][j] stores the number of paths from cell (0,0) to cell (i,j)
    T = [[0 for x in range(n)] for y in range(m)]
 
    # There is only one way to reach any cell in the first column i.e. to move down
    for i in range(m):
        T[i][0] = 1
 
    # There is only one way to reach any cell in the first row i.e. to move right
    for j in range(n):
        T[0][j] = 1
 
    # fill T in bottom-up manner
    for i in range(1, m):
        for j in range(1, n):
            T[i][j] = T[i-1][j] + T[i][j-1]
 
    # last cell of T stores the count of paths from cell(0,0) to cell(i,j)
    return T[m-1][n-1]
 
 
if __name__ == '__main__':
 
    # M x N matrix
    M = N = 3
 
    k = countPaths(M, N)
    print("Total number of paths are:", k)