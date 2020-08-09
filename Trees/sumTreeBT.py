
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
# Data structure to store a Binary Tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
 
# Function to print pre-order traversal of given tree
def preorder(root):
 
    if root is None:
        return
 
    print(root.data, end=' ')
    preorder(root.left)
    preorder(root.right)
 
 
# Recursive function to in-place convert the given binary tree to its
# sum tree by traversing the tree in post-order manner
def convertToSumTree(root):
 
    # base case: tree is empty
    if root is None:
        return 0
 
    # recursively convert left and right subtree first before
    # processing the root node
    left = convertToSumTree(root.left)
    right = convertToSumTree(root.right)
 
    # stores current value of root node
    old = root.data
 
    # update root to sum of left and right subtree
    root.data = left + right
 
    # return the updated value plus old value (sum of tree rooted at root node)
    return root.data + old
 
 
if __name__ == '__main__':
 
    root = None
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
 
    convertToSumTree(root)
    preorder(root)
 