def knapsack(w, v,n, W):
    if W < 0:
        return float('-inf')
    if n < 0 or W==0:
        return 0
    include = v[n] + knapsack(w,v,n-1,W-w[n])
    exclude = knapsack(w,v,n-1,W)
    return max(include, exclude)
def knapsackMemoized(w, v,n, W):
    if W < 0:
        return float('-inf')
    if n < 0 or W==0:
        return 0
    key = (n,W)
    if key not in lookup:

        include = v[n] + knapsack(w,v,n-1,W-w[n])
        exclude = knapsack(w,v,n-1,W)
        lookup[key] = max(include, exclude)
    return lookup[key]

def knapsackDP(w,v,n, W):
    T = [[0 for j in range(W+1)] for i in range(len(v)+1)]
    for i in range(1, len(v)+1):
        for j in range(W+1):
            if (w[i-1] > j):
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = max(T[i-1][j], v[i-1] + T[i-1][j-w[i-1]])
  
    return T[len(v)][W]



lookup = {}
if __name__=='__main__':
    v = [20, 5, 10, 40, 15, 25]
    w = [1,2,3,8,7,4]
    W = 10
    
    print(knapsackDP(w,v,len(w)-1,W))