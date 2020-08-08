def printList(list):
	for (num, sign) in list:
		print(f"({sign}){num}", end=' ')
	print()


# Print all ways to calculate a target from elements of specified list
def printWays(A, n, sum, target, list):

	# base case: if target is found, print result list
	if sum == target:
		printList(list)
		return

	# base case: No elements are left
	if n < 0:
		return

	# Ignore the current element
	printWays(A, n - 1, sum, target, list)

	# Consider the current element and subtract it from the target
	list.append((A[n], '+'))
	printWays(A, n - 1, sum + A[n], target, list)
	list.pop()  # backtrack

	# Consider the current element and add it to the target
	list.append((A[n], '-'))
	printWays(A, n - 1, sum - A[n], target, list)
	list.pop()  # backtrack


if __name__ == '__main__':

	# input list and target number
	A = [5, 3, -6, 2]
	target = 6

	printWays(A, len(A) - 1, 0, target, [])