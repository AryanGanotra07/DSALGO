# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

def inorder(a, res, B):
    if a is None:
        return 
    inorder(a.left, res, B)
    res.append(a.val)
    if res[0] + res[-1] == B:
        return 1
    inorder(a.right, res, B)
    
    return 0

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def t2Sum(self, A, B):
        
        stack=[]
        result=[]
        node=A
        while(stack or node):
            if node:
                stack.append(node)
                node=node.left
            else:
                node=stack.pop()
                result.append(node.val)
                node=node.right
        i=0
        j=len(result)-1
        while(i<len(result) and j>0 and j>i):
            if(result[i]+result[j]<B):
                i+=1
            elif(result[i]+result[j]>B):
                j-=1
            elif(result[i]+result[j]==B):
                return(1)
        else:
            return(0)
        # i = 0
        # j = len(res) - 1
        # while i < j:
        #     if res[i] + res[j] == B:
        #         return 1
        #     if res[i] + res[j] > B:
        #         j-=1
        #     elif res[i] + res[j] < B:
        #         i+=1
        # return 0
                
