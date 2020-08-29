# Bottom-up DP function to mark if X[i..j] is a palindrome
# or not for all possible values of i and j
def findAllPalindromes(X, isPalin):

	for i in reversed(range(len(X))):
		for j in range(i, len(X)):
			if i == j:
				isPalin[i][j] = True
			elif X[i] == X[j]:
				isPalin[i][j] = True if (j - i == 1) else isPalin[i + 1][j - 1]
			else:
				isPalin[i][j] = False


# Recursive function to find the minimum cuts needed in a String
# such that each partition is a palindrome
def minPalinPartition(i, j, isPalin, lookup):

	# base case: if starting index i and ending index j are equal
	# or X[i..j] is already a palindrome.
	if i == j or isPalin[i][j]:
		return 0

	# construct an unique dict key from dynamic elements of the input
	# lookup[key] stores minimum number cuts needed to partition X[i..j]
	key = (i, j)

	# if sub-problem is seen for the first time, solve it and
	# store its result in a dict
	if key not in lookup:

		# take the minimum over each possible position at which the can be cut

		"""
			(X[i]) | (X[i+1..j])
			(X[i..i+1]) | (X[i+2..j])
			(X[i..i+2]) | (X[i+3..j])
			...
			...
			(X[i..j-1]) | (X[j])
		"""

		lookup[key] = float('inf')
		for k in range(i, j):
			# recur to get minimum cuts required in X[i..k] and X[k+1..j]
			count = 1 + minPalinPartition(i, k, isPalin, lookup) + \
					minPalinPartition(k + 1, j, isPalin, lookup)

			if count < lookup[key]:
				lookup[key] = count

	# return the minimum cuts required
	return lookup[key]


if __name__ == '__main__':

	X = "BABABCBADCD"

	# create a dictionary to store solutions of subproblems
	lookup = {}

	# isPalin[i][j] stores if subX[i][j] is palindrome or not
	isPalin = [[False for x in range(len(X) + 1)] for y in range(len(X) + 1)]

	# find all substrings of X that are palindromes
	findAllPalindromes(X, isPalin)

	print("The minimum cuts required are", 
			minPalinPartition(0, len(X) - 1, isPalin, lookup))
