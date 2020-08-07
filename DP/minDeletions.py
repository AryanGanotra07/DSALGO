def minDeletions(X, n):
 
    # Y is reverse of X
    Y = X[::-1]
 
    # lookup[i][j] stores the length of LCS of substring
    # X[0..i-1], Y[0..j-1]
    lookup = [[0 for x in range(n + 1)] for y in range((n + 1))]
 
    # fill the lookup table in bottom-up manner
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # if current character of X and Y matches
            if X[i - 1] == Y[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + 1
 
            # else if current character of X and Y don't match
            else:
                lookup[i][j] = max(lookup[i - 1][j], lookup[i][j - 1])
 
    # Now lookup[n][n] contains the size of the Longest Palindromic Subsequence
 
    # The minimum number of deletions required will be size of the String
    # minus size of the Palindromic Subsequence
 
    return n - lookup[n][n]
 
 
if __name__ == '__main__':
 
    X = "ACBCDBAA"
    n = len(X)
 
    print("The minimum number of deletions required are", minDeletions(X, n))