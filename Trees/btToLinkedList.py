# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
sys.setrecursionlimit(15000000)
def solve(a, b):
    if a is None:
        return 
    b.append(a.val)
    solve(a.left, b)
    solve(a.right, b)

def solve(a):
    if a is None or (a.left is None and a.right is None):
        return None
    if a.left is not None:
        solve(a.left)
        tmp = a.right
        a.right = a.left
        a.left = None
        b = a.right
        while b.right is not None:
            b= b.right
        b.right = tmp
    solve(a.right)
        
    

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, A):
        solve(A)
        return A
        # b = []
        # solve(A, b)
        
        # r = TreeNode(b[0])
        # n = r
        # for i in range(1, len(b)):
        #     n.right = TreeNode(b[i])
        #     n = n.right
        # return r
        
    
        
