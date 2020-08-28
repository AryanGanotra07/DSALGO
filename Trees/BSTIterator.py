# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.arr = []
        self.preorder(root)
        self.n = len(self.arr)
        self.cnt = 0
    def preorder(self, root):
        if root is None:
            return 
        self.preorder(root.left)
        self.arr.append(root.val)
        self.preorder(root.right)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if self.cnt < self.n - 1:
            return True
        return False
        

    # @return an integer, the next smallest number
    def next(self):
        a = self.arr[self.cnt]
        self.cnt+=1
        return a
        

# Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print i.next(),
