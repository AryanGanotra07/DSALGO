def isPalindrome(s, i, j):
    s = s[i:j+1]
    return s == s[::-1]
def partition(s, i, j):
    if i >= j:
        return 0
    if (isPalindrome(s,i, j)):
        return 0
    mn = float('inf')
    for k in range(i, j):
        cost = partition(s, i, k)
        cost += partition(s, k+1, j)
        cost += 1
        if mn > cost:
            mn = cost
    return mn
#memoize is palidrome too
def partitionOptimized(s, i, j):
    if i >= j :
        return 0
    key = (i, j)
    if key not in lookup:
        mn = float('inf')
        if (isPalindrome(s, i, j)):
            lookup[key] = 0
            return lookup[key]
        for k in range(i, j):
            kl = (i, k)
            if kl not in lookup:
                lookup[kl] = partition(s, i, k)
            kr = (k+1, j)
            if kr not in lookup:
                lookup[kr] = partition(s, k+1, j)
            cost = lookup[kl] + lookup[kr] + 1
            if mn > cost:
                mn = cost
        lookup[key] = mn
    return lookup[key]



lookup = {}

if __name__ == "__main__":
    s = "nitik"
    print(partitionOptimized(s, 0, len(s) -1))

