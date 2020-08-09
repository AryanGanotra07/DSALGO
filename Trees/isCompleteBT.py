
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
81
82
83
from collections import deque
 
 
# Data structure to store a Binary Tree node
class Node:
    def __init__(self, key=None, left=None, right=None):
 
        self.key = key
        self.left = left
        self.right = right
 
 
# Function to check if given Binary Tree is Complete or not
def isComplete(root):
    if root is None:
        return True
    q = deque()
    q.append(root)
    flag = False
    while q:
        t = q.popleft()
        if flag and (t.left or t.right):
            return False
        if t.left is None and t.right:
            return False
        if t.left:
            q.append(t.left)
        else:
            flag = True
        if t.right:
            q.append(t.right)
        else:
            flag = True
    return True

 
 
if __name__ == '__main__':
 
    """ Construct below tree
              1
           /     \
          2       3
         / \     / \
        4   5   6   7
    """
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
 
    if isComplete(root):
        print("Given Binary Tree is a Complete Binary Tree")
    else:
        print("Given Binary Tree is not a Complete Binary Tree")
 