# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        from collections import deque
        q = deque()
        q.append(A)
        ans = []
        while len(q):
            t = q.popleft()
            while t:
                ans.append(t.val)
                if t.left:
                    q.append(t.left)
                t = t.right
        return ans
            
