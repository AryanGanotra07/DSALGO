
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    def maxDepth(self, A):
        if A == None :
            return 0
        return 1 + max(self.maxDepth(A.left), self.maxDepth(A.right))
    
sol = Solution()
sol.maxDepth(TreeNode(1))