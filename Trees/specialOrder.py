from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    

def solve(x):
    if x is None:
        return 
    print(x.val, end = " ")
    q1 = deque()
    q2 = deque()
    q1.append(x.left)
    q2.append(x.right)
    while(q1):
        n = len(q1)
        for _ in range(n):
            t = q1.popleft()
            print(t.val, end = " ")
            if t.left:
                q1.append(t.left)
            if t.right:
                q1.append(t.right)
            y = q2.popleft()
            print(y.val, end = " ")
            if y.right:
                q2.append(y.right)
            if y.left:
                q2.append(y.left)

if __name__ == '__main__':

	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.left = Node(6)
	root.right.right = Node(7)
	root.left.left.left = Node(8)
	root.left.left.right = Node(9)
	root.left.right.left = Node(10)
	root.left.right.right = Node(11)
	root.right.left.left = Node(12)
	root.right.left.right = Node(13)
	root.right.right.left = Node(14)
	root.right.right.right = Node(15)

	solve(root)

