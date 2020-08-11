arr = [12, 1, 12, 3, 12, 1, 1, 2, 3, 2, 2, 3, 7]
n = len(arr)
res = 0
for i in range(32):
    sm = 0
    x = 1 << i
    for j in range(n):
        if (arr[j]& x):
            sm+=1
    if sm % 3:
        res = res | x
print(res)