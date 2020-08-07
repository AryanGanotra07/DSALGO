# Function that matches input with given wildcard pattern
def isMatching(str, pattern, n, m, lookup):
 
    # If both input string and pattern reaches their end,
    # return True
    if m < 0 and n < 0:
        return True
 
    # If only pattern reaches its end, return false
    elif m < 0:
        return False
 
    # If only input string reaches its end, return true
    # if remaining characters in the pattern are all '*'
    elif n < 0:
        for i in range(m + 1):
            if pattern[i] != '*':
                return False
        return True
 
    # If the sub-problem is encountered for the first time
    if not lookup[n][m]:
        if pattern[m] == '*':
            # 1. * matches with current characters in input string.
            # Here we will move to next character in the string
 
            # 2. Ignore * and move to next character in the pattern
            lookup[n][m] = isMatching(str, pattern, n - 1, m, lookup) or \
                           isMatching(str, pattern, n, m - 1, lookup)
        else:
            # If the current character is not a wildcard character, it
            # should match with current character in the input string
            if pattern[m] != '?' and pattern[m] != str[n]:
                lookup[n][m] = False
            # check if pattern[0..m-1] matches str[0..n-1]
            else:
                lookup[n][m] = isMatching(str, pattern, n - 1, m - 1, lookup)
 
    return lookup[n][m]

def isMatching(str, pattern):
 
    # get length of and wildcard pattern
    n = len(str)
    m = len(pattern)
 
    # create a DP lookup table
    T = [[False for x in range(m + 1)] for y in range(n + 1)]
 
    # if both pattern and is empty : match
    T[0][0] = True
 
    # handle empty case (i == 0)
    for j in range(1, m + 1):
        if pattern[j - 1] == '*':
            T[0][j] = T[0][j - 1]
 
    # build matrix in bottom-up manner
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if pattern[j - 1] == '*':
                T[i][j] = T[i - 1][j] or T[i][j - 1]
            elif pattern[j - 1] == '?' or str[i - 1] == pattern[j - 1]:
                T[i][j] = T[i - 1][j - 1]
 
    # last cell stores the answer
    return T[n][m]
 
 
if __name__ == '__main__':
 
    str = "xyxzzxy"
    pattern = "x***x?"
 
    # create a DP lookup table
    lookup = [[False for x in range(len(pattern) + 1)] for y in range(len(str) + 1)]
 
    if isMatching(str, pattern):
        print("Match")
    else:
        print("No Match")