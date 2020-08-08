# Calculate the size of the largest '+' formed by 1's
def calculateSize(grid):

	# left[j][j] stores maximum number of consecutive 1's
	# present to the left of grid[i][j] (including grid[i][j])
	left = [[0 for x in range(N)] for y in range(N)]

	# right[j][j] stores maximum number of consecutive 1's
	# present to the right of grid[i][j] (including grid[i][j])
	right = [[0 for x in range(N)] for y in range(N)]

	# top[j][j] stores maximum number of consecutive 1's
	# present to the top of grid[i][j] (including grid[i][j])
	top = [[0 for x in range(N)] for y in range(N)]

	# bottom[j][j] stores maximum number of consecutive 1's
	# present to the bottom of grid[i][j] (including grid[i][j])
	bottom = [[0 for x in range(N)] for y in range(N)]

	# initialize above matrices
	for i in range(N):
		# initialize first row of top matrix
		top[0][i] = grid[0][i]

		# initialize last row of bottom matrix
		bottom[N - 1][i] = grid[N - 1][i]

		# initialize first column of left matrix
		left[i][0] = grid[i][0]

		# initialize last column of right matrix
		right[i][N - 1] = grid[i][N - 1]

	# fill all cells of above four matrix
	for i in range(N):
		for j in range(1, N):
			# fill left matrix
			if grid[i][j] == 1:
				left[i][j] = left[i][j - 1] + 1

			# fill top matrix
			if grid[j][i] == 1:
				top[j][i] = top[j - 1][i] + 1

			# fill bottom matrix
			if grid[N - 1 - j][i] == 1:
				bottom[N - 1 - j][i] = bottom[N - j][i] + 1

			# fill right matrix
			if grid[i][N - 1 - j] == 1:
				right[i][N - 1 - j] = right[i][N - j] + 1

	# bar stores length of longest + found so far
	bar = 0

	# compute longest plus
	for i in range(N):
		for j in range(N):
			# find minimum of left(i, j), right(i, j), top(i, j), bottom(i, j)
			len = min(top[i][j], bottom[i][j], left[i][j], right[i][j])

			# largest + would be formed by a cell that has maximum value
			if len - 1 > bar:
				bar = len - 1

	return bar


if __name__ == '__main__':

	grid = [
		[1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
		[1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
		[1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
		[0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
		[1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
		[1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
		[1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
		[1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
		[1, 0, 1, 1, 1, 1, 0, 1, 0, 0]
	]

	N = 10
	bar = calculateSize(grid)

	# 4 directions of length 4*bar + 1 for middle cell
	if bar:
		print("Largest Plus of 1's has size of", (4 * bar + 1))
