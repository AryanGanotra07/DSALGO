
def rodCuttingRecursive(price, n):
    if n <= 0:
        return 0
    
    maxValue = float('-inf')
    for i in range(1, n+1):
        cost = price[i-1] + rodCuttingRecursive(price, n-i)
        if cost > maxValue:
            maxValue = cost
    
    return maxValue

def rodCuttingDP(price, n):
    T = [0]*(n+1)
    for i in range(1, n+1):
        for j in range(1,i+1):
            T[i] = max(T[i], price[j-1] + T[i-j])
    return T[n]

def rodCuttingDP2(length,price, n):
    T = [[0 for i in range(n+1)] for j in range(len(length)+1)]
    for i in range(1,len(length)+1):
        for j in range(1,n+1):
            if (length[i-1] > j):
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = max(T[i-1][j], price[i-1] + T[i][j-length[i-1]])
    return T[len(length)][n]




if __name__ == '__main__':
    length = [1,2,3,4,5,6,7,8]
    prices = [1,5,8,9,10,17,17,20]
    n = 4
    print(rodCuttingDP2(length,prices, n))
    pass