#code
import sys
sys.setrecursionlimit(15000)
def find(v, t):
    r = len(t)
    c = len(t[0])
    for i in range(r):
        for j in range(c):
            if t[i][j] == v:
                return [i, j]
    return None
def isPath(src, dest, t, n, lk):
    i = src[0]
    j = src[1]
    di = dest[0]
    dj = dest[1]
    key = (i, j)
    if key in lk:
        return lk[key]
    if i==di and j == dj:
        return True
    if i < 0 or j < 0 or i >= n or j >= n:
        return False
    if t[i][j] == 0:
        return False
    up = isPath([i-1,j], dest, t, n,lk)
    down = isPath([i+1, j], dest, t, n,lk)
    left = isPath([i, j-1], dest, t, n, lk)
    right = isPath([i, j+1], dest, t, n, lk)
    lk[key] = left or right or up or down
    return lk[key]
    

for t in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    col = n
    t = [l[i:i+col] for i in range(0, len(l), col)]
    src = find(1, t)
    dest = find(2, t)
    if src is None or dest is None:
        print(0)
    lk = {}
    if isPath(src, dest, t, n,lk):
        print(1)
    else:
        print(0)
    
            