# Function to check if the given string is K-Palindrome or not
def isKPalindrome(X, K):
 
    # Y is reverse of X
    Y = X[::-1]
 
    n = len(X)
 
    # lookup table to store solution of already computed sub-problems
    T = [[0 for x in range(n + 1)] for y in range((n + 1))]
 
    # fill the lookup table T in bottom-up manner
    for i in range(n + 1):
        for j in range(n + 1):
            # if either string is empty, remove all characters from
            # other string
            if i == 0 or j == 0:
                T[i][j] = i + j
 
            # ignore last characters of both strings if they are same
            # and process remaining characters
            elif X[i - 1] == Y[j - 1]:
                T[i][j] = T[i - 1][j - 1]
 
            # if last character of both strings is different, consider
            # minimum by removing last character from the X and Y
            else:
                T[i][j] = 1 + min(T[i - 1][j], T[i][j - 1])
 
    return T[n][n] <= 2 * K
 
 
if __name__ == '__main__':
 
    str = "CABCBC"
    K = 2
 
    if isKPalindrome(str, K):
        print("String is K-Palindrome")
    else:
        print("String is not a K-Palindrome")