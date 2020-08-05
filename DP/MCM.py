def MCMRecursive(dims, i, j):
    if i + 1 >=j :
        return 0
    mn = float('inf')
    for k in range(i + 1, j):
 
        # recur for M[i+1]..M[k] to get an i x k matrix
        cost = MCMRecursive(dims, i, k)
 
        # recur for M[k+1]..M[j] to get a k x j matrix
        cost += MCMRecursive(dims, k, j)
 
        # cost to multiply two (i x k) and (k x j) matrix
        cost += dims[i] * dims[k] * dims[j]
 
        if cost < mn:
            mn = cost
    return mn

def MCMMemoized(dims, i, j):
    if i + 1 >= j:
        return 0
    mn = float('inf')
    for k in range(i+1, j):
        if k not in lookup:
                # recur for M[i+1]..M[k] to get an i x k matrix
            cost = MCMRecursive(dims, i, k)
    
            # recur for M[k+1]..M[j] to get a k x j matrix
            cost += MCMRecursive(dims, k, j)
    
            # cost to multiply two (i x k) and (k x j) matrix
            cost += dims[i] * dims[k] * dims[j]
            lookup[k] = cost
        if lookup[k] < mn:
            mn = lookup[k]
    return mn
            
 


lookup = {}
if __name__ == '__main__':
 
    # Matrix M[i] has dimension dims[i-1] x dims[i] for i = 1..n
    # input is 10 × 30 matrix, 30 × 5 matrix, 5 × 60 matrix
    dims = [10, 30, 5, 60]
 
    print("Minimum cost is", MCMMemoized(dims, 0, len(dims) - 1))