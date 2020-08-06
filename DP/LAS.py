def solve(arr,st,flag):
    res = 0
    for i in range(st, len(arr)):

        if flag and arr[i] > arr[i-1]:
            res = max(res, 1 + solve(arr, i+1,False))
        elif flag == False and arr[i] < arr[i-1]:
            res =  max(res, solve(arr, i+1, True) + 1)
        else:
            res = max(res, solve(arr, i+1, flag) )
        
    return res
def longest(arr):
    n = len(arr)
    return 1 + max(solve(arr, 1, True), solve(arr, 1, False))

def longestDP(arr):
    t = [[0]*2 for r in range(len(arr)+1)]
    res =0 
    t[0][1] = t[0][0] = 1
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                t[i][0] = max(t[i][0], t[j][1] + 1)
            elif arr[i] < arr[j]:
                t[i][1] = max(t[i][1], t[j][0] + 1)
        if res < max(t[i][0], t[i][1]):
            res = max(t[i][0], t[i][1])
    return res 

 
if __name__ == '__main__':
 
    A = [8, 9, 6, 4, 5, 7, 3, 2, 4]
 
    print("The length of Longest Subsequence is", longestDP(A))