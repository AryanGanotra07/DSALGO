from collections import deque
class Node:
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None


def reverseLevelOrderTraversal(root):

	if root is None:
		return

	# create an empty queue and enqueue root node
	queue = deque()
	queue.append(root)

	# create a stack to reverse level order nodes
	stack = deque()

	# loop till queue is empty
	while queue:

		# process each node in queue and enqueue their children
		curr = queue.popleft()

		# push current node to stack
		stack.append(curr.key)

		# important - process right node before left node
		if curr.right:
			queue.append(curr.right)

		if curr.left:
			queue.append(curr.left)

	# pop all nodes from the stack and print them
	while stack:
		print(stack.pop(), end=' ')


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    reverseLevelOrderTraversal(root)
    
