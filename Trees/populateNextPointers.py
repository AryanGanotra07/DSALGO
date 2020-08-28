# Definition for a  binary tree node
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        from collections import deque
        if root is None:
            return root
        q = deque()
        q.append(root)
        a = root
        while len(q):
            n = len(q)
            prev = None
            for i in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if prev is None:
                    prev = node
                else:
                    prev.next = node
                    prev = prev.next
        
        
        
