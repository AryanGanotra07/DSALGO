class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


from collections import deque

def leftView(x):
    if x is None:
        return
    q = deque()
    q.append(x)
    while(q):
        i = 0
        n = len(q)
        while(i < n):
            t = q.popleft()
            i+=1
            if i == 1:
                print(t.val, end = " ")
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)

if __name__ == '__main__':

	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.right = Node(4)
	root.right.left = Node(5)
	root.right.right = Node(6)
	root.right.left.left = Node(7)
	root.right.left.right = Node(8)

	leftView(root)

