def lbs(a):
    n = len(a)
    I = [0]*n
    D = [0]*n
    I[0] = 1
    for i in range(1, n):
        for j in range(i):
            if (a[i] > a[j] and I[i] < I[j]):
                I[i] = I[j]
        I[i]+=1
    D[n-1] = 1
    for i in reversed(range( n-1)):
        for j in range(n-1,i,-1):
            if (a[i]  > a[j] and D[i] < D[j]):
                D[i] = D[j]
        D[i]+=1
    lb = 1
    for i in range(n):
        lb = max(lb, I[i] + D[i] - 1)
    return lb
if __name__ == '__main__':
 
    A = [4, 2, 5, 9, 7, 6, 10, 3, 1]
 
    print("Length of Longest Bitonic Subsequence is", lbs(A))
        
    