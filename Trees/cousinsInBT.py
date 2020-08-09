
# Data structure to store a Binary Tree node
class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
 
 
# Data structure to store a Binary Tree node along
# with its level and parent information
class NodeInfo:
    def __init__(self, key, level, parent):
        self.key = key
        self.level = level
        self.parent = parent
 
 
# Perform in-order traversal of the binary tree and update x and y
def inorder(root, parent, level, x, y):
    if root is None:
       return None
    inorder(root.left, root, level + 1, x, y)
    if x and x.key == root.key:
        x.level = level
        x.parent = parent
    if y and y.key == root.key:
        y.level = level
        y.parent = parent
    inorder(root.right, root, level + 1, x, y)
 
 
# Function to determine if two given nodes are cousins of each other
def iterative(root, elem1, elem2):
    if root is None:
       return False
    level = 1
    x = NodeInfo(elem1, 1, None)
    y = NodeInfo(elem2, 1, None)
    inorder(root, None, level, x, y)
    if x and y and (x.level == y.level) and x.parent != y.parent:
        return True
    return False
 
 
if __name__ == '__main__':
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
 
    if iterative(root, 5, 6):
        print("Given nodes are cousins")
    else:
        print("Given nodes are not cousins")
 