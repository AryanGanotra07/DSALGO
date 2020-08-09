class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def findHD(x, l):
    if x is None:
        return 
    if l not in lookup:
        lookup[l] = []
    lookup[l].append(x.val)
    if x.left:
        findHD(x.left, l-1)
    
    if x.right:
        findHD(x.right, l+1)
    
    


lookup = {}

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
    findHD(root, 0)
    print(lookup)
    for i in sorted(lookup.keys()):
        print(lookup[i][-1], end = " ")



