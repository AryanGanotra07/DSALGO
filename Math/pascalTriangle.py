def solve(A):
    n = A
    b = []
    for i in range(1, n+1):
        b.append([0]*i)
    for line in range(1, n+1):
        C = 1
        for i in range(1, line+1):
            b[line-1][i-1] = C
            C = int(C*(line - i)/i)
    return b

print(solve(5))