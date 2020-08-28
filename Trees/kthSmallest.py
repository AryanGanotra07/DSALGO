# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
def inorder(A, res):
    if A is None:
        return 
    inorder(A.left, res)
    res.append(A.val)
    inorder(A.right, res)

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        res = []
        inorder(A,res)
        if B > len(res):
            return -1
        return res[B-1]
