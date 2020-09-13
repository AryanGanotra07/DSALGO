class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


def rightView(root):
    '''
    :param root: root of given tree.
    :return: print the right view of tree, dont print new line
    '''
    # code here
    from collections import deque
    q = deque()
    q.append(root)
    ans = []
    while q:
        n = len(q)
        for i in range(n):
            t = q.popleft()
            if i==n-1:
                ans.append(str(t.data))
            if t.left is not None:
                q.append(t.left)
            if t.right is not None:
                q.append(t.right)
    print(" ".join(ans))

root = Node(9)
root.left = Node(10)
root.right = Node(39)
root.left.right = Node(40)
root.right.left = Node(55)
root.right.right = Node(5)
root.left.right.right = Node(3)
root.right.left.left = Node(16)
root.right.left.right = Node(19)
root.right.right.right = Node(16)
root.left.right.right.left = Node(29)
root.left.right.right.right = Node(37)
rightView(root)

