from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def ltor(x, level):
    if x is None:
        return False
    if level == 1:
        print (x.val, end = " ")
        return True
    left = ltor(x.left, level - 1)
    right = ltor(x.right, level-1)
    return left or right

def rtol(x, level):
    if x is None:
        return False
    if level == 1:
        print(x.val, end = " ")
        return True
    right = rtol(x.right, level-1)
    left = rtol(x.left, level-1)
    return left or right


def spiralOrder(x):
    if x is None:
        return 
    level  = 1
    process = True
    while process:
        process = ltor(x, level)
        level+=1
        if process:
            process = rtol(x, level)
            level += 1


def spiralOrderTraversal(root):
 
    if root is None:
        return
 
    # create an empty ended queue and enqueue root node
    q = deque()  # or use deque
    q.appendleft(root)
 
    # flag used to differentiate between odd or even level
    flag = False
 
    # loop till deque is empty
    while q:
 
        # calculate number of nodes in current level
        nodeCount = len(q)
 
        # print left to right
        if flag:
            # process each node of current level and enqueue their
            # non-empty left and right child to deque
            while nodeCount > 0:
                # pop from front if flag is True
                curr = q.popleft()
                print(curr.val, end=' ')
 
                # push left child to end followed by right child if flag is True
 
                if curr.left:
                    q.append(curr.left)
 
                if curr.right:
                    q.append(curr.right)
 
                nodeCount = nodeCount - 1
 
        # print right to left
        else:
            # process each node of current level and enqueue their
            # non-empty right and left child to queue
            while nodeCount > 0:
                # Important - pop from back if flag is False
                curr = q.pop()
                print(curr.val, end=' ')
 
                # print front node
                # Important - push right child to front followed by left
                # child if flag is False
 
                if curr.right:
                    q.appendleft(curr.right)
 
                if curr.left:
                    q.appendleft(curr.left)
 
                nodeCount = nodeCount - 1
 
        # flip the flag for next level
        flag = not flag
        print()
 








lookup = {}

if __name__ == '__main__':

	root = Node(15)
	root.left = Node(10)
	root.right = Node(20)
	root.left.left = Node(8)
	root.left.right = Node(12)
	root.right.left = Node(16)
	root.right.right = Node(25)

	spiralOrderTraversal(root)

