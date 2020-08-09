
class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
 
 
# Recursive function to check if given binary tree is a sum tree or not
def isSumTree(root):
 
    # base case: empty tree
    if root is None:
        return 0
 
    # special case: leaf node
    if root.left is None and root.right is None:
        return root.key
 
    # if root's value is equal to sum of all elements present in its
    # left and right subtree
    if root.key == isSumTree(root.left) + isSumTree(root.right):
        return 2 * root.key
 
    return float('-inf')
 
 
if __name__ == '__main__':
 
    """ Construct below tree
             44
            /  \
           /    \
          9     13
         / \    / \
        4   5  6   7
    """
 
    root = Node(44)
    root.left = Node(9)
    root.right = Node(13)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
 
    if isSumTree(root) != float('-inf'):
        print("Yes")
    else:
        print("No")