# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        from collections import deque
        q = deque()
        q.append(A)
        res = []
        d = True
        while len(q):
            n = len(q)
            tmp = []
            for i in range(n):
                if d == False:
                    a = q.pop()
                    tmp.append(a.val)
                    if a.right:
                        q.appendleft(a.right)
                    if a.left:
                        q.appendleft(a.left)
                else:
                    a = q.popleft()
                    tmp.append(a.val)
                    if a.left:
                        q.append(a.left)
                    if a.right:
                        q.append(a.right)
            res.append(tmp)
            d = not d
        return res
