# Function to check whether (i, x) and (i, y) are valid matrix coordinates
def isValid(i, x, y):
	return i < M and 0 <= x < N and 0 <= y < N


# Collect maximum coins from cell (i, x) to cell (M-1, 0) and from
# cell (i, y) to cell (M-1, N-1)
def maxCoins(mat, i, x, y):

	# return if either (i, x) or (i, y) is invalid
	if not isValid(i, x, y):
		return float('-inf')

	# current row is the last row
	if i == M - 1:
		# destination reached
		if x == 0 and y == N - 1:
			return mat[i][x] if (x == y) else mat[i][x] + mat[i][y]

		# destination not reached
		return float('-inf')

	# stores the max number of coins
	coins = float('-inf')

	# recur for all possible ways:
	# (i, x) . (i+1, x-1) or (i+1, x) or (i+1, x+1)
	# (i, y) . (i+1, y-1) or (i+1, y) or (i+1, y+1)

	coins = max(coins, maxCoins(mat, i + 1, x - 1, y - 1))
	coins = max(coins, maxCoins(mat, i + 1, x - 1, y))
	coins = max(coins, maxCoins(mat, i + 1, x - 1, y + 1))

	coins = max(coins, maxCoins(mat, i + 1, x, y - 1))
	coins = max(coins, maxCoins(mat, i + 1, x, y))
	coins = max(coins, maxCoins(mat, i + 1, x, y + 1))

	coins = max(coins, maxCoins(mat, i + 1, x + 1, y - 1))
	coins = max(coins, maxCoins(mat, i + 1, x + 1, y))
	coins = max(coins, maxCoins(mat, i + 1, x + 1, y + 1))

	# update max number of coins with current cell coins before returning
	if x == y:
		return mat[i][x] + coins
	else:
		return (mat[i][x] + mat[i][y]) + coins


if __name__ == '__main__':

	mat = [
		[0, 2, 4, 1],
		[4, 8, 3, 7],
		[2, 3, 6, 2],
		[9, 7, 8, 3],
		[1, 5, 9, 4]
	]

	(M, N) = (len(mat), len(mat[0]))

	# start with the cells (0, 0) and (0, N-1)
	print("The maximum coins collected is", maxCoins(mat, 0, 0, N - 1))
