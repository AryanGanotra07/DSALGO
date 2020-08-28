# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def _isSymmetric(self, a, b):
        if a is None:
            return b is None
        if b is None:
            return a is None
        return a.val == b.val and \
            self._isSymmetric(a.right, b.left) and \
            self._isSymmetric(a.left, b.right)
    
    # @param A : root node of tree
    # @return an integer
    def isSymmetric(self, A):
        return 1 if self._isSymmetric(A.left, A.right) else 0
