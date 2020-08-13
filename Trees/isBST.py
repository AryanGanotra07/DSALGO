class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def isBST(root):
    return isBSTUtil(root, float('-inf'), float('inf'))
    

def isBSTUtil(root, mn, mx):
    if root == None:
        return True
    if root.val < mn or root.val > mx:
        return False
    return isBSTUtil(root.left, mn, root.val - 1) and isBSTUtil(root.right, root.val+1, mx)

root = Node(4) 
root.left = Node(2) 
root.right = Node(1) 
root.left.left = Node(1) 
root.left.right = Node(3) 
  
if (isBST(root)): 
    print( "Is BST")
else: 
    print( "Not a BST")