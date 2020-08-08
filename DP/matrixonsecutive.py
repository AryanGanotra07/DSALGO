# Below lists details all 8 possible movements
row = [-1, -1, -1, 0, 0, 1, 1, 1]
col = [-1, 0, 1, -1, 1, -1, 0, 1]


# check whether cell (x, y) is valid or not
def isValid(x, y):
	return 0 <= x < M and 0 <= y < N


# Find length of longest path in the matrix mat with consecutive characters
# The path should continue from the previous character
# Here (i, j) denotes the coordinates of the current cell
def findMaxLength(mat, x, y, previous):

	# base case: return length 0 if current cell (x, y) is invalid or
	# current character is not consecutive to the previous character
	if not isValid(x, y) or chr(ord(previous) + 1) != mat[x][y]:
		return 0

	# stores the length of longest path
	max_len = 0

	# recur for all 8 adjacent cells from current cell
	for k in range(8):

		# visit position (x + row[k], y + col[k]) and find maximum length from that path
		length = findMaxLength(mat, x + row[k], y + col[k], mat[x][y])

		# update the length of longest path if required
		max_len = max(max_len, 1 + length)

	return max_len


# Find length of longest path in the matrix with consecutive characters
def findMaximumLength(mat, ch):

	# stores the length of longest path
	max_len = 0

	# traverse the matrix
	for x in range(M):
		for y in range(N):
			# start from the current cell if its value matches with given character
			if mat[x][y] == ch:
				# recur for all 8 adjacent cells from current cell
				for k in range(8):
					# visit position (x + row[k], y + col[k]) and
					# find maximum length from that path
					length = findMaxLength(mat, x + row[k], y + col[k], ch)

					# update the length of longest path if required
					max_len = max(max_len, 1 + length)

	return max_len


if __name__ == '__main__':

	# input matrix
	mat = [
		['D', 'E', 'H', 'X', 'B'],
		['A', 'O', 'G', 'P', 'E'],
		['D', 'D', 'C', 'F', 'D'],
		['E', 'B', 'E', 'A', 'S'],
		['C', 'D', 'Y', 'E', 'N']
	]

	# Size of given matrix is M x N
	(M, N) = (len(mat), len(mat[0]))

	# starting character
	ch = 'C'

	print("The length of longest path with consecutive characters starting from "
		  "character", ch, "is", findMaximumLength(mat, ch))
