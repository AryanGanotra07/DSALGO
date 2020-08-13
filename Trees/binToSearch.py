class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder(root, a):
    if root is None:
        return 
    inorder(root.left, a)
    a.append(root.val)
    inorder(root.right, a)

def convertInorder(root, a):
    if root is None:
        return 
    convertInorder(root.left, a)
    root.val = a[0]
    a.pop(0)
    convertInorder(root.right, a)

def printInorder(root): 
    if root is None: 
        return
    printInorder(root.left) 
    print (root.val, end = " ")  
    printInorder(root.right) 

def convert(root):
    a = []
    inorder(root, a)
    a.sort()
    convertInorder(root, a)

root = Node(10) 
root.left = Node(30) 
root.right = Node(15) 
root.left.left = Node(20) 
root.right.right = Node(5) 
convert(root)
printInorder(root)



    