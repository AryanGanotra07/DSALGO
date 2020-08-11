def solve(arr):
    n = len(arr)
    r = 0
    for i in range(n):
        r ^= arr[i]
    return r

a = [1,2,2,4,5,6,6,5,1]
print(solve(a))
