
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
from collections import deque
 
 
# Data structure to store a Binary Tree node
class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
 
 
# Function to find next node of given node in the same level
# in given binary tree
def findRightNode(root, val):
 
    # return None if tree is empty
    if root is None:
        return None
 
    # create an empty queue and enqueue root node
    queue = deque()
    queue.append(root)
 
    # loop till queue is empty
    while queue:
 
        # calculate number of nodes in current level
        size = len(queue)
 
        # process every node of current level and enqueue their
        # non-empty left and right child to queue
        while size > 0:
            size = size - 1
            front = queue.popleft()
 
            # if desired node is found, return its next right node
            if front.key == val:
                # if next right node doesn't exists, return None
                if size == 0:
                    return None
 
                return queue[-1]
 
            if front.left:
                queue.append(front.left)
 
            if front.right:
                queue.append(front.right)
 
    return None

def findRightNode(root, value, level, value_level):
 
    # return None if tree is empty
    if root is None:
        return None, value_level
 
    # if desired node is found, set value_level to current level
    if root.data == value:
        return None, level
 
    # if value_level is already set, then current node is the next right node
    elif value_level:
        if level == value_level:
            return root, level
 
    # recur for left subtree by increasing level by 1
    left, value_level = findRightNode(root.left, value, level + 1, value_level)
 
    # if node is found in left subtree, return it
    if left:
        return left, value_level
 
    # recur for right subtree by increasing level by 1
    return findRightNode(root.right, value, level + 1, value_level)
 
 
# Function to find next node of given node in the same level
# in given binary tree
def findRightNodeBT(root, value):
 
    value_level = 0
    return findRightNode(root, value, 1, value_level)[0]
 
 
if __name__ == '__main__':
 
    """ Construct below Tree
              1
            /  \
           /    \
          2      3
         / \      \
        4   5      6
                  / \
                 7   8
    """
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
 
    right = findRightNode(root, 5)
    if right:
        print("Right is", right.key)
    else:
        print("Right doesn't exists")
 