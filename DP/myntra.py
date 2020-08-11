
def solve(cost, i, prev):
    if i >= len(cost):
        return 0
    mn = float('inf')
    val = 0
    if prev != 0:
        
        mn = min(mn, solve(cost, i+1, 0)+cost[i][0])
        
    if prev != 1:
         
        mn = min(mn, solve(cost, i+1, 1)+cost[i][1])
       
    if prev != 2:
        
        mn = min(mn, solve(cost, i+1, 2)+cost[i][2])
        
    return mn

def solveMemoized(cost, i, prev):
    if i >= len(cost):
        return 0
    mn = float('inf')
    val = 0
    key = (i, prev)
    if key in lookup:
        return lookup[key]
    
    if prev != 0:
        
        mn = min(mn, solve(cost, i+1, 0)+cost[i][0])
        
    if prev != 1:
         
        mn = min(mn, solve(cost, i+1, 1)+cost[i][1])
       
    if prev != 2:
        
        mn = min(mn, solve(cost, i+1, 2)+cost[i][2])
    lookup[key] = mn
    return mn

lookup = {}






if __name__ == "__main__":
    cost = [[1,10,100], [2,100,1000]]
    print(solveMemoized(cost, 0, -1))
