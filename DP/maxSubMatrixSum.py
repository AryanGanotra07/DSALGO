# Find maximum sum submatrix present in a given matrix
def findMaxSumSubmatrix(matrix):

	# M x N matrix
	(M, N) = (len(matrix), len(matrix[0]))

	# S[i][j] stores sum of sub-matrix formed by row 0 to i-1
	# and column 0 to j-1
	S = [[0 for x in range(N + 1)] for y in range(M + 1)]

	# pre-process the matrix to fill S
	for i in range(1, M + 1):
		for j in range(1, N + 1):
			S[i][j] = S[i - 1][j] + S[i][j - 1] - S[i - 1][j - 1] \
                      + matrix[i - 1][j - 1]

	maxSum = float('-inf')
	rowStart = rowEnd = colStart = colEnd = 0

	# consider every sub-matrix formed by row i to j
	# and column m to n
	for i in range(M):
		for j in range(i, M):
			for m in range(N):
				for n in range(m, N):
					# calculate sub-matrix sum using S in O(1) time
					submatrix_sum = S[j + 1][n + 1] - S[j + 1][m] \
                                    - S[i][n + 1] + S[i][m]

					# if sub-matrix sum is more than maximum found so far
					if submatrix_sum > maxSum:
						maxSum = submatrix_sum
						rowStart = i
						rowEnd = j
						colStart = m
						colEnd = n

	print("Sub-matrix is formed by row", rowStart, "to", rowEnd, 
          "and column from", colStart, "to", colEnd)
	return maxSum


# Find maximum sum sub-matrix
if __name__ == '__main__':

	# input matrix
	matrix = [
		[-5, -6, 3, 1, 0],
		[9, 7, 8, 3, 7],
		[-6, -2, -1, 2, -4],
		[-7, 5, 5, 2, -6],
		[3, 2, 9, -5, 1]
	]

	# find maximum sum sub-matrix
	print("The maximum sum of sub-matrix is", findMaxSumSubmatrix(matrix))
