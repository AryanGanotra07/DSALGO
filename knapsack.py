def knapsack(w, v,n, W):
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
lookup = {}
if __name__=='__main__':
    v = [20, 5, 10, 40, 15, 25]
    w = [1,2,3,8,7,4]
    W = 10
    
    print(knapsack(w,v,len(w)-1,W))