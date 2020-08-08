# Function to find LCS of list X[0..m-1] and Y[0..n-1]
def LCS(X, Y, m, n):

	# return if we have reached the end of either list
	if m == 0 or n == 0:
		return

	# if last element of X and Y matches
	if X[m - 1] == Y[n - 1]:
		LCS(X, Y, m - 1, n - 1)
		print(X[m - 1], end=' ')
		return

	# else when the last element of X and Y are different

	if lookup[m - 1][n] > lookup[m][n - 1]:
		LCS(X, Y, m - 1, n)
	else:
		LCS(X, Y, m, n - 1)


# Function to find length of Longest Common Subsequence of
# list X[0..m-1] and Y[0..n-1]
def findLCS(X, Y, m, n):

	# first row and first column of the lookup table
	# are already 0 as lookup is globally declared

	# fill the lookup table in bottom-up manner
	for i in range(1, m + 1):
		for j in range(1, n + 1):

			# if current element of X and Y matches
			if X[i - 1] == Y[j - 1]:
				lookup[i][j] = lookup[i - 1][j - 1] + 1

			# else if current element of X and Y don't match
			else:
				lookup[i][j] = max(lookup[i - 1][j], lookup[i][j - 1])

	# find longest common sequence
	LCS(X, Y, m, n)


# Function to remove duplicates from a sorted list
def removeDuplicates(X):

	k = 0
	for i in range(1, len(X)):
		if X[i] != X[k]:
			k = k + 1
			X[k] = X[i]

	# return length of sublist containing all distinct characters
	return k + 1


# Iterative function to find length of longest increasing subsequence (LIS)
# of given list using longest common subsequence (LCS)
def findLIS(X):

	# create a sorted copy of the original list
	Y = sorted(X.copy())

	# remove all the duplicates from Y
	m = removeDuplicates(Y)

	# perform LCS of both
	findLCS(X, Y, len(X), m)


# Longest Increasing Subsequence using LCS
if __name__ == '__main__':

	X = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

	# N is maximum possible length of X and Y
	N = len(X) + 1

	# lookup[i][j] stores the length of LCS of sublist X[0..i-1], Y[0..j-1]
	lookup = [[0 for x in range(N)] for y in range(N)]

	print("The LIS is: ", end='')
	findLIS(X)
