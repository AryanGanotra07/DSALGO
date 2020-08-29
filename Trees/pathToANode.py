# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

def solve(a, curr, b):
    if a is None:
        return False
    curr.append(a.val)
    if a.val == b:
        return True
    
    left = solve(a.left, curr, b)
    if left:
        return curr
    right = solve(a.right, curr, b)
    if right:
        return curr
    curr.pop()
    
    
        

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        curr = []
        solve(A,curr, B)
        return curr
            
