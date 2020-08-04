def eggDrop(e,f):
    if (f == 0 or f == 1):
        return f
    if (e == 0):
        return f
    ans = float('inf')
    for k in range(1, f+1):
        cnt = 1 + max(eggDrop(e-1, k-1), eggDrop(e, f-k)) 
        ans = min(ans, cnt)
    return ans

if __name__ == "__main__":
    e = 2
    f = 10
    print(eggDrop(e,f))
