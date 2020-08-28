# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

        

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def verticalOrderTraversal(self, A):
        m={}
        m=self.sol(A,m,0,0)
        ans=[]
        k=[]
        for y in sorted(m):
            m[y]=sorted(m[y],key=lambda x:x[0])
            s=[]
            for i in m[y]:
                s.append(i[1])
            ans.append(s)
        return ans
        
            
        
    def sol(self,root,m,h,l):
        if root is None:
            return m
        if h in m:
            m[h].append([l,root.val])
        else:
            m[h]=[[l,root.val]]
        m=self.sol(root.left,m,h-1,l+1)
        m=self.sol(root.right,m,h+1,l+1)
        return m
            
            
