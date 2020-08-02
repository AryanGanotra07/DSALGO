def LISRecursive(a,s, n, prev):
    if s == n:
        return 0
    excl = LISRecursive(a, s+1, n, prev)
    incl = 0
    if prev < a[s]:
        incl = LISRecursive(a, s+1, n, a[s]) + 1
    return max(incl, excl)

if __name__ == '__main__':
 
    A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
 
    print("Length of LIS is", LISRecursive(A, 0, len(A), float('-inf')))
    