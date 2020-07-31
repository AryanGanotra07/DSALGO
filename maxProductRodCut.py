
def maxProductRecursive(n):
    if (n==0):
        return 0
    
    mx = n
    for i in range(1, n+1):
        mx = max(mx, i*maxProductRecursive(n-i))
    return mx


def maxProductDP(n):
    T = [i for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, i+1):
            T[i] = max(T[i], j*T[i-j])
    return T[n]

# def maxProductDP2(n):
#     T = [[i for j in range(n+1)] for i in range(n+1) ]
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             T[i][j] = i
#             if (i > j):
#                 T[i][j] = T[i-1][j]
#             else:
#                 T[i][j] = max(i, j*T[i][j-i])
#     return T[n][n]



if __name__ == '__main__':
    print(maxProductDP2(15))
    pass