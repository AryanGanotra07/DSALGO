# Find optimal cost to construct binary search tree from keys i to j
# where each key k occurs freq[k] number of times
def findOptimalCost(freq, i, j, level, lookup):

	# base case
	if j < i:
		return 0

	# construct an unique dict key from dynamic elements of the input
	key = (i, j, level)

	# if sub-problem is seen for the first time, solve it and
	# store its result in a dict
	if key not in lookup:

		lookup[key] = float('inf')

		# consider each key as root and recursively find optimal solution
		for k in range(i, j + 1):
			# recursively find the optimal cost of left subtree
			leftOptimalCost = findOptimalCost(freq, i, k - 1, level + 1, lookup)

			# recursively find the optimal cost of right subtree
			rightOptimalCost = findOptimalCost(freq, k + 1, j, level + 1, lookup)

			# current node's cost is freq[k]*level

			# update optimal cost
			lookup[key] = min(lookup[key], freq[k] * level + leftOptimalCost
											+ rightOptimalCost)

	# return the sub-problem solution from the dict
	return lookup[key]


if __name__ == '__main__':

	freq = [25, 10, 20]

	# create a dictionary to store solutions of sub-problems
	lookup = {}

	print("The optimal cost of constructing BST is",
			findOptimalCost(freq, 0, len(freq) - 1, 1, lookup))
