from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def isIdentical(x, y):
    if x is None and y is None:
        return True
    return (x and y ) and x.val == y.val and isIdentical(x.left, y.left) and isIdentical(x.right, y.right)

def isIdenticalIterative(x,y):
    if x == None and y is None:
        return True
    if x is None:
        return False
    if y is None:
        return False
    if x != y:
        return False
    stack = deque()
    stack.append((x, y))
    while stack:
		(x, y) = stack.pop()
		if x.key != y.key:
			return False
		if x.left and y.left:
			stack.append((x.left, y.left))
		elif x.left or y.left:
			return False
		if x.right and y.right:
			stack.append((x.right, y.right))
		elif x.right or y.right:
			return False
    return True


if __name__ == "__main__":
    # construct first tree
	x = Node(15)
	x.left = Node(10)
	x.right = Node(20)
	x.left.left = Node(8)
	x.left.right = Node(12)
	x.right.left = Node(16)
	x.right.right = Node(25)

	# construct second tree
	y = Node(15)
	y.left = Node(10)
	y.right = Node(20)
	y.left.left = Node(8)
	y.left.right = Node(12)
	y.right.left = Node(16)
	y.right.right = Node(15)

	if isIdentical(x, y):
		print("Given Binary Trees are identical")
	else:
		print("Given Binary Trees are not identical")


