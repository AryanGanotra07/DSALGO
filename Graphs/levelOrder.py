class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None


def levelOrder(A):
    nodes = {}
    discover(A, 0 ,nodes)
    print(nodes)
    

def discover(A, level, nodes):
    if A == None:
        return None
    if level not in nodes:
        nodes[level] = []
    
    nodes[level].append(A.val)
    discover(A.left, level+1, nodes)
    discover(A.right, level+1, nodes)
    

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
levelOrder(root)
