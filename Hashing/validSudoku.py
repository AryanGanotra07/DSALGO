def isValidSudoku(self, A):
    for i in range(len(A)):
        d = {}
        for j in range(len(A[0])):
            if A[i][j]!=".":
                x = A[i][j]
                if x in d:
                    return 0
                else:
                    d[x] = 1
    for j in range(len(A[0])):
        d = {}
        for i in range(len(A)):
            if A[i][j]!= ".":
                x = A[i][j]
                if x in d:
                    return 0
                else:
                    d[x] = 1
    d = {}
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j]!=".":
                key = (i//3, j//3)
                if key in d:
                    if d[key].count(A[i][j]) == 0:
                        d[key].append(A[i][j])
                    else:
                        return 0
                else:
                    d[key] = []
                    d[key].append(A[i][j])
    return 1