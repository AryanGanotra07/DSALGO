# Construct maximum length snake sequence from given tail and L matrix
def constructPath(L, grid, tail):

	(i, j) = tail
	path = [tail]

	# start from snake's tail till snake's head
	while L[i][j]:
		if i - 1 >= 0 and L[i][j] - L[i - 1][j] == 1 and \
                abs(grid[i - 1][j] - grid[i][j]) == 1:
			path.append((i - 1, j))
			i = i - 1
		elif j - 1 >= 0 and L[i][j] - L[i][j - 1] == 1 and \
                abs(grid[i][j - 1] - grid[i][j]) == 1:
			path.append((i, j - 1))
			j = j - 1

	return path


# Function to find maximum length of snake sequence in given matrix
def findMaxLengthSnakeSequence(grid):

	# L[i][j] stores the maximum length of snake sequence
	# ending at cell (i, j)
	L = [[0 for x in range(len(grid))] for y in range(len(grid))]

	# stores maximum length of Snake sequence
	max_so_far = 0

	# Pair to store coordinates of snake's tail
	tail = None

	# process the matrix in bottom-up fashion
	for i in range(len(grid)):
		for j in range(len(grid)):
			# compare current cell with top cell and check absolute difference
			if i - 1 >= 0 and abs(grid[i - 1][j] - grid[i][j]) == 1:
				L[i][j] = L[i - 1][j] + 1
				if max_so_far < L[i][j]:
					max_so_far = L[i][j]
					tail = (i, j)

			# compare current cell with left cell and check absolute difference
			if j - 1 >= 0 and abs(grid[i][j - 1] - grid[i][j]) == 1:
				# L[i][j] can be non-zero at this point, hence take maximum
				L[i][j] = max(L[i][j], L[i][j - 1] + 1)
				if max_so_far < L[i][j]:
					max_so_far = L[i][j]
					tail = (i, j)

	# construct maximum length snake sequence
	return constructPath(L, grid, tail)


if __name__ == '__main__':

	grid = [
		[7, 5, 2, 3, 1],
		[3, 4, 1, 4, 4],
		[1, 5, 6, 7, 8],
		[3, 4, 5, 8, 9],
		[3, 2, 2, 7, 6]
	]

	path = findMaxLengthSnakeSequence(grid)
	print("Maximum length Snake sequence: ", end='')

	# use reverse range to print the List (from snake head to tail)
	print([grid[x][y] for x, y in path][::-1])
	print("Length is:", len(path) - 1)
