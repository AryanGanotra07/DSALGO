def findSubmatrixSum(mat, p, q, r, s):

	# pre-process the input matrix such that sum[i][j] stores
	# sum of elements in matrix from (0, 0) to (i, j)
	sum = [[0 for x in range(len(mat[0]))] for y in range(len(mat))]
	sum[0][0] = mat[0][0]

	# pre-process first row
	for j in range(1, len(mat[0])):
		sum[0][j] = mat[0][j] + sum[0][j - 1]

	# pre-process first column
	for i in range(1, len(mat)):
		sum[i][0] = mat[i][0] + sum[i - 1][0]

	# pre-process rest of the matrix
	for i in range(1, len(mat)):
		for j in range(1, len(mat[0])):
			sum[i][j] = mat[i][j] + sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1]

	# total = sum[r][s] - sum[r][q - 1] - sum[p - 1][s] + sum[p - 1][q - 1]
	total = sum[r][s]

	if q - 1 >= 0:
		total -= sum[r][q - 1]

	if p - 1 >= 0:
		total -= sum[p - 1][s]

	if p - 1 >= 0 and q - 1 >= 0:
		total += sum[p - 1][q - 1]

	return total


if __name__ == '__main__':

	mat = [
		[0, 2, 5, 4, 1],
		[4, 8, 2, 3, 7],
		[6, 3, 4, 6, 2],
		[7, 3, 1, 8, 3],
		[1, 5, 7, 9, 4]
	]

	# (p, q) and (r, s) represents top-left and bottom-right
	# coordinates of the sub-matrix
	p = q = 1
	r = s = 3

	# calculate sub-matrix sum
	print(findSubmatrixSum(mat, p, q, r, s))
