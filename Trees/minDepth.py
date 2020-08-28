# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def solve(node):
    if node is None:
        return float('inf')
    if node.left is None and node.right is None:
        return 1
    left = 1+solve(node.left)
    right =1+solve(node.right)
    return min(left, right)
    

class Solution:
    # @param A : root node of tree
    # @return an integer
    def minDepth(self, A):
        return solve(A)
