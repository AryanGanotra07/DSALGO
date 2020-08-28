# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return a list of list of integers
	def pathSum(self, A, B):
	    res = []
        def solve(curr_set,curr_sum,node):
            nonlocal res
            if node is None:
                return 
            if node.right is None and node.left is None:
                if curr_sum+node.val==B:
                    res.append(curr_set+[node.val])
                    return
                else:
                    return
            solve(curr_set+[node.val],curr_sum+node.val,node.left)
            solve(curr_set+[node.val],curr_sum+node.val,node.right)
        solve([],0,A)
        return res
