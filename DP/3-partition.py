def partition(A, n):
    if len(A) < 3:
        return False
    return sum(A)%3==0 and partitionMemoized(A, n,sum(A)//3 , sum(A)//3, sum(A)//3)

def partitionRecursion(A,n,a,b,c):
    if a==0 and b==0 and c==0:
        return True
    if n < 0 :
        return False
    
    aa = False
    if (a-A[n] >= 0):
        aa = partitionRecursion(A, n-1, a - A[n], b, c)
    bb = False
    if not aa and (b-A[n] >= 0):
        bb = partitionRecursion(A, n-1, a, b- A[n], c)
    cc = False
    if (aa != True and bb!=True) and (c-A[n]>=0):
        cc = partitionRecursion(A, n-1, a, b, c - A[n])
    return aa or  bb or cc 

def partitionMemoized(A, n, a, b, c):
    if a==0 and b==0 and c==0:
        return True
    if n < 0 :
        return False
    key = (n,a,b,c)
    if key not in lookup:
        aa = False
        if (a-A[n] >= 0):
            aa = partitionRecursion(A, n-1, a - A[n], b, c)
        bb = False
        if not aa and (b-A[n] >= 0):
            bb = partitionRecursion(A, n-1, a, b- A[n], c)
        cc = False
        if (aa != True and bb!=True) and (c-A[n]>=0):
            cc = partitionRecursion(A, n-1, a, b, c - A[n])
        lookup[key] = aa or  bb or cc 
    return lookup[key]

lookup = {}


    
    

if __name__ == '__main__':
    A = [7,3,2,1,5,4,8]
    print(partition(A, len(A)-1))