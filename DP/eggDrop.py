def eggDrop(e,f):
    if (f == 0 or f == 1):
        return f
    if (e == 0):
        return f
    key = (e,f)
    if key in lookup:
        return lookup[key]
    ans = float('inf')
    for k in range(1, f+1):
        kb = (e-1, k-1)
        if kb not in lookup:
            lookup [kb] = eggDrop(e-1, k-1)
        kt = (e, f-k)
        if kt not in lookup:
            lookup[kt] = eggDrop(e, f-k)
        cnt = 1 + max(lookup[kb], lookup[kt]) 
        ans = min(ans, cnt)
    lookup[key] = ans
    return ans

lookup = {}

if __name__ == "__main__":
    e = 2
    f = 10
    print(eggDrop(e,f))
