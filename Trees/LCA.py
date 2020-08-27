# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

def solve(A, B, C):
    if A is None:
        return None
    if A.val == B or A.val == C:
        return A
    l = solve(A.left, B, C)
    r = solve(A.right, B, C)
    if l is not None and r is not None:
        return A
    if l:
        return l
    
    return r
def search(A, B):
    if A is None:
        return False
    if A.val == B:
        return True
    return search(A.left, B) or search(A.right, B)
    

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def lca(self, A, B, C):
        if search(A, B) and search(A,C):
            pass
        else:
            return -1
        s = solve(A, B, C)
        if s is not None:
            return s.val
        return -1
