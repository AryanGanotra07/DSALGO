def paranthesize(s, i, j, e):
    if i > j :
        return 0
    if i == j:
        if e == True and s[i] == "T":
            return 1
        elif e == False and s[i] == "F":
            return 1
        else:
            return 0
    ans = 0 
    for k in range(i+1, j , 2):
        lt = paranthesize(s, i, k-1, True)
        lf = paranthesize(s, i , k-1, False)
        rt = paranthesize(s, k+1, j, True)
        rf = paranthesize(s, k+1, j, False)
        if s[k] == '&':
            if e == True:
                ans += lt * rt
            else:
                ans += lt * rf + lf * rf + lf * rt
        elif s[k] == '|':
            if e == True:
                ans += lt * rt + lt * rf + lf * rt
            else:
                ans += lf * rf
        elif s[k] == '^':
            if e == True:
                ans += lt * rf + lf * rt
            else:
                ans += lt * rt + lf * rf
    return ans

if __name__ == "__main__":
    s = "T|T&F^T"
    print(paranthesize(s, 0, len(s)-1, True))
     

