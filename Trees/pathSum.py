# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def solve(A, B):
    if not A:
        return 0
    if not A.left and not A.right:
        return 1 if A.val==B else 0
    return solve(A.left,B-A.val) or solve(A.right,B-A.val)

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self, A, B):
        return 1 if solve(A,B) else 0
