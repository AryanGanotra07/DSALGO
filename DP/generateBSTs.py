# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution:
    # @param A : integer
    # @return a list of TreeNode 
    def generateTrees(self, A):
        if A == 0:
            return []
        return self._generateTrees(1, A + 1)

    # generates all the trees starting from start to end
    def _generateTrees(self, start, end):
        trees = []
        for i in range(start, end):
            for left in self._generateTrees(start, i):
                for right in self._generateTrees(i + 1, end):
                    trees.append(TreeNode(i))
                    trees[-1].left = left
                    trees[-1].right = right
        return trees if trees else [None]
