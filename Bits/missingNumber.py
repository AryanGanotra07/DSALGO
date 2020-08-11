a = [1,2,3,4,5,6,7,9,10]

def solve(arr):
    a = 1
    b = arr[0]
    n = len(arr)
    for i in range(2, n+2):
        a^=i
    for i in range(1,n):
        b^=arr[i]
    return a^b

print(solve(a))