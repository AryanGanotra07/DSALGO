from collections import deque
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Recursive function to perform pre-order traversal of the tree
def preorder(root):

    # return if the current node is empty
    if root is None:
        return

    # Display the data part of the root (or current node)
    print(root.data, end=' ')

    # Traverse the left subtree
    preorder(root.left)

    # Traverse the right subtree
    preorder(root.right)

	# preorder(root.left)

	# # Traverse the right subtree
	# preorder(root.right)

# Iterative function to perform in-order traversal of the tree
def preorderIterative(root):

	
    # return if tree is empty
    if root is None:
        return

    # create an empty stack and push root node
    stack = deque()
    stack.append(root)

    # loop till stack is empty
    while stack:

        # pop a node from the stack and print it
        curr = stack.pop()

        print(curr.data, end=' ')

        # push right child of popped node to the stack
        if curr.right:
            stack.append(curr.right)

        # push left child of popped node to the stack
        if curr.left:
            stack.append(curr.left)

    # important note - right child is pushed first so that left child
    # is processed first (FIFO order)



