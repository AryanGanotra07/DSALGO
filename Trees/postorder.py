from collections import deque
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Recursive function to perform post-order traversal of the tree
def postorder(root):

    # return if the current node is empty
    if root is None:
        return

    # Traverse the left subtree
    postorder(root.left)

    # Traverse the right subtree
    postorder(root.right)

    # Display the data part of the root (or current node)
    print(root.data, end=' ')

def postorderIterative(root):

    # create an empty stack and push root node
    stack = deque()
    stack.append(root)

    # create another stack to store post-order traversal
    out = deque()

    # loop till stack is empty
    while stack:

        # we pop a node from the stack and push the data to output stack
        curr = stack.pop()
        out.append(curr.data)

        # push left and right child of popped node to the stack
        if curr.left:
            stack.append(curr.left)

        if curr.right:
            stack.append(curr.right)

    # print post-order traversal
    while out:
        print(out.pop(), end=' ')


