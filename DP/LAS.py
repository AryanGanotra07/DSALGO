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

 
if __name__ == '__main__':
 
    A = [8, 9, 6, 4, 5, 7, 3, 2, 4]
 
    print("The length of Longest Subsequence is", longest(A))