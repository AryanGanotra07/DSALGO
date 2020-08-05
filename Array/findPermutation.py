def solve(A, B):
    l = []
    i = 1
    j = B
    for s in A:
        if s == 'I':
            l.append(i)
            i+=1
        else:
            l.append(j)
            j-=1
    l.append(i)
    return l

print(solve("ID",3 ))