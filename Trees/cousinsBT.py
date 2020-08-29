# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

def solve(a,curr, level, res):
    if a is None or curr > level:
        return 
    if curr == level:
        res.append(a.val)
    solve(a.left, curr+1, level, res)
    solve(a.right, curr+1, level, res)

def search(a, b, level):
    if a is None:
        return -1
    if a.val == b:
        return level
    left = search(a.left, b, level+1)
    right = search(a.right, b, level+1)
    if left != -1:
        return left
    else:
        if right!=-1:
            return right
    return -1
class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        if A==B:
            return []
        q=[]
        res=[]
        q.append(A)
        boo=False
        i=1
        while(q and not boo):
            size=len(q)
            
            while(size):
                p=q[0]
                q=q[1:]
                
                if (p.left and p.left.val==B) or (p.right and p.right.val==B):
                    boo=True
    
                else:
                    if p.left:q.append(p.left)
                    if p.right:q.append(p.right)
                
                size-=1
            
        if boo:
            for i in q:
                res.append(i.val)
        return res