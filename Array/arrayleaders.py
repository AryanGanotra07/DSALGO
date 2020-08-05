def solve(A):
    mx = float('-inf')
    res = []
    for i in range(len(A)-1, -1, -1):
        if (A[i] > mx):
            res.append(A[i])
        mx = max(mx, A[i])
    res.reverse()
    return res

print(solve([16, 17, 4, 3, 5, 2]))