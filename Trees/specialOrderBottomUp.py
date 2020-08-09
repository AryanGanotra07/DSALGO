from collections import deque
 
 
# Data structure to store a Binary Tree node
class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
 
 
# Function to print all nodes of a given binary tree in
# specific order from bottom to top
def printNodes(root):
 
    # return is tree is empty
    if root is None:
        return
 
    # start with level 1 (of root node)
    level = 1
 
    # create an empty multi-dict of integers (every key can be
    # associated with multiple values)
    dict = {}
 
    # insert root node at first level
    dict.setdefault(level, []).append(root.key)
 
    # create a two empty queues and enqueue root's left and
    # right child respectively
    q1 = deque()
    q2 = deque()
 
    q1.append(root.left)
    q2.append(root.right)
 
    # loop till queue is empty
    while q1:
 
        # increment level by 1
        level = level + 1
 
        # calculate number of nodes in current level
        n = len(q1)
 
        # process every node of current level
        while n > 0:
 
            # pop front node from first queue and insert it into the dict
            x = q1.popleft()
            dict.setdefault(level, []).append(x.key)
 
            # push left and right child of x to first queue
            if x.left:
                q1.append(x.left)
 
            if x.right:
                q1.append(x.right)
 
            # pop front node from second queue and insert it into the dict
            y = q2.popleft()
 
            dict.get(level).append(y.key)
 
            # push right and left child of y to second queue
            if y.right:
                q2.append(y.right)
 
            if y.left:
                q2.append(y.left)
 
            n = n - 1
 
    # iterate through the dictionary and print all nodes present in very level
    for i in reversed(dict.keys()):
        print(dict.get(i), end='')
 
 
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
 
    printNodes(root)