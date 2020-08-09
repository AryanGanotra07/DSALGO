class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


from collections import deque

def levelOrder(x, level):
    if x is None:
        return
    if level not in lookup:
        lookup[level] = []
    lookup[level].append(x.val)
    if x.left is not None:
        levelOrder(x.left, level + 1)
    if x.right is not None:
        levelOrder(x.right,level+1)

def levelorderIter(x, level):
    if x is None:
        return 
    q = deque()
    q.append(x)
    while(q):
        t = q.popleft()
        print(t.val , end = ' ')
        if t.left:
            q.append(t.left)
        if t.right:
            q.append(t.right)
    
    


lookup = {}

if __name__ == "__main__":
    x = Node(1)
    x.left = Node(2)
    x.right = Node(3)
    x.left.left = Node(4)
    x.left.right = Node(5)
    levelorderIter(x, 0)
    # print(lookup)
