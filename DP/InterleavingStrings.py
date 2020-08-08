# Function to check if X and Y are interleaving of S or not
def interleaved(X, Y, S):

	# return true if we have reached end of all Strings
	if not X and not Y and not S:
		return True

	# return false if we have reached the end of S
	# but X or Y are not empty
	if not S:
		return False

	# if X is not empty and its first character matches with
	# first character of S, recur for remaining substring
	x = (len(X) and S[0] == X[0]) and interleaved(X[1:], Y, S[1:])

	# if Y is not empty and its first character matches with
	# first character of S, recur for remaining substring
	y = (len(Y) and S[0] == Y[0]) and interleaved(X, Y[1:], S[1:])

	return x or y

def interleaved(X, Y, S):
	M, N = len(X), len(Y)

	# base case: length of given strings doesn't match
	if M + N != len(S):
		return False

	# Create a lookup table T[][] to store solution to already computed sub-problems
	# T[i][j] is True when S[0..i+j-1] is an interleaving of X[0..i-1] and Y[0..j-1]
	T = [[False for x in range(N + 1)] for y in range(M + 1)]

	# fill the lookup table in bottom-up manner
	for i in range(0, M + 1):
		for j in range(0, N + 1):

			if i == 0 and j == 0:			# both strings are empty
				T[i][j] = True

			# if current char of S matches with the current char of both A and B
			elif i and j and X[i - 1] == S[i + j - 1] and Y[j - 1] == S[i + j - 1]:
				T[i][j] = T[i - 1][j] or T[i][j - 1]

			# if current char of X matches with the current char of S
			elif i and X[i - 1] == S[i + j - 1]:
				T[i][j] = T[i - 1][j]

			# if current char of Y matches with the current char of S
			elif j and Y[j - 1] == S[i + j - 1]:
				T[i][j] = T[i][j - 1]

	# T[M][N] stores the result
	return T[M][N]


if __name__ == '__main__':

	X = "ABC"
	Y = "ACD"
	S = "ACDABC"

	if interleaved(X, Y, S):
		print("Given String is interleaving of X and Y")
	else:
		print("Given String is a not interleaving of X and Y")
