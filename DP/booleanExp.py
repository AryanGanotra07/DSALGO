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

def paranthesizeMem(s, i, j , e):
    if i > j:
        return 0
    if i == j:
        if e == True and s[i] == "T":
            return 1
        elif e == False and s[i] == "F":
            return 1
        else:
            return 0
    key = (i, j, e)
    if key not in lookup:
        ans = 0 
        for k in range(i+1, j , 2):
            klt = (i, k-1, True)
            klf = (i, k-1, False)
            krt = (k+1, j, True)
            krf = (k+1, j, False)
            if klt not in lookup:
                lookup[klt] = paranthesize(s, i, k-1, True)
            if klf not in lookup:
                lookup[klf] = paranthesize(s, i , k-1, False)
            if krt not in lookup:
                lookup[krt] = paranthesize(s, k+1, j, True)
            if krf not in lookup:
                lookup[krf] = paranthesize(s, k+1, j, False)
            if s[k] == '&':
                if e == True:
                    ans += lookup[klt] * lookup[krt]
                else:
                    ans += lookup[klt] * lookup[krf] + lookup[klf] * lookup[krf] + lookup[klf] * lookup[krt]
            elif s[k] == '|':
                if e == True:
                    ans += lookup[klt] * lookup[krt] + lookup[klt] * lookup[klf] + lookup[krt] * lookup[klf]
                else:
                    ans += lookup[klf] * lookup[krf]
            elif s[k] == '^':
                if e == True:
                    ans += lookup[klt] * lookup[krf] + lookup[klf] * lookup[krt]
                else:
                    ans += lookup[klt] * lookup[krt] + lookup[klt] * lookup[klf]
        lookup[key] = ans
    return lookup[key]
    
    
    

lookup = {}

if __name__ == "__main__":
    s = "T|T&F^T"
    print(paranthesizeMem(s, 0, len(s)-1, True))
     

