def solve(A, B):
    if B==0:
        return 0
    if len(A)//2 <=B:
        m=0
        for i in range(1,len(A)):
            if A[i]>A[i-1]:
                m+= A[i]-A[i-1]
        return m
        
    buy =[float('-inf') for i in range(B) ]
    sell = [0 for i in range(B) ]
    for i in range(len(A)):
        for j in range(B):
            buy[j] = max(buy[j], -A[i] if j==0 else sell[j-1] - A[i]  )
            sell[j] = max(sell[j] , buy[j]+ A[i])
    return sell[-1]
A = [3, 2, 6, 5, 0, 3]
B = 2
print(solve(A,B))