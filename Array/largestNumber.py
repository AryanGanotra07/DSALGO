from functools import cmp_to_key
def comp(a,b):
    a1 = int(str(a)+str(b))
    a2 = int(str(b)+str(a))
    if a1 > a2:
        return -1 
    elif a1 < a2 :
        return 1
    else:
        return 0
def solve(A):
    A.sort(key=cmp_to_key(comp))
    res= ""
    for i in A:
        res+=str(i)
    return res

print(solve([3, 30, 34, 5, 9]))