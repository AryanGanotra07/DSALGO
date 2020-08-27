# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def solve(a, mx, mn):
    if a is None:
        return True
    if a.val < mn or a.val > mx:
        return False
    return solve(a.left, a.val - 1, mn) and solve(a.right, mx, a.val+1)

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isValidBST(self, A):
        return 1 if solve(A, float('inf'), float('-inf')) else 0 
