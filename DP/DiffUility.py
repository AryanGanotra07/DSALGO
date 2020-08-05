def LCSDP(s1, s2, m, n, T):
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if (s1[i-1] == s2[j-1]):
                T[i][j] = 1 + T[i-1][j-1]
            else:
                T [i][j] = max(T[i-1][j], T[i][j-1])
    return T

def diff(x,y,m,n,T):
    if m > 0 and n > 0 and x[m-1] == y[n-1]:
        diff(x,y,m-1,n-1,T)
        print("", x[m-1], end = "")
    elif n > 0 and (m==0 or T[m][n-1] >= T[m-1][n]):
        diff(x,y,m,n-1,T)
        print(" +", y[n-1], end = "")
    elif m > 0 and (n==0 or T[m-1][n] > T[m][n-1]):
        diff(x,y,m-1, n,T)
        print(" -", x[m-1], end = "")

    
        
    

if __name__ == '__main__':
 
    X = "ABCDFGHJQZ"
    Y = "ABCDEFGIJKRXYZ"
    m = len(X)
    n = len(Y)
 
    # lookup[i][j] stores the length of LCS of subX[0..i-1], Y[0..j-1]
    T = [[0 for j in range(n+1)] for i in range(m+1)]
 
    # fill lookup table
    LCSDP(X, Y, m, n, T)
 
    # find difference
    diff(X, Y, m, n, T)
