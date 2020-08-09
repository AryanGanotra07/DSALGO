from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def height(x):
    if x is None:
        return 0
    return 1 + max(height(x.left) ,height(x.right))

def heightIterative(x):
    if x is None:
        return 0
    hl = 0
    xl = x
    while(xl):
        hl += 1
        xl = xl.left
    hr = 0
    xr = x
    while(xr):
        hr += 1
        xr = xr.right 
    return max(hl, hr)
        

if __name__ == '__main__':

	root = Node(15)
	root.left = Node(10)
	root.right = Node(20)
	root.left.left = Node(8)
	root.left.right = Node(12)
	root.right.left = Node(16)
	root.right.right = Node(25)

	print("The height of the binary tree is", heightIterative(root))
