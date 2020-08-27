# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

def solve(i, l):
    if i > len(l)-1:
        return None
    temp = TreeNode(l[i])
    temp.left = solve(2*i+1, l)
    temp.right = solve(2*i+2, l)
    return temp
def solve(root,A,  parent, left, right):
    if root == -1:
        return None
    temp = TreeNode(A[root])
    temp.left = solve(left[root], A, parent, left, right)
    temp.right = solve(right[root], A, parent, left, right)
    return temp
    

class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def buildTree(self, A):
        n= len(A)
        parent = [-1]*n
        left = [-1]*n
        right = [-1]*n
        root = 0
        last = 0
        for i in range(1,n):
            last = i-1
            right[i] = -1
            while(A[last] <= A[i] and last!=root):
                last = parent[last]
            if A[last] <= A[i]:
                parent[root] = i
                left[i] = root
                root = i
            elif right[last] == -1:
                right[last] = i
                parent[i] = last
                left[i] = -1
            else:
                parent[right[last]] = i
                left[i] = right[last]
                right[last] = i
                parent[i] = last
        parent[root] = -1
        return solve(root,A, parent, left, right)
        # a = TreeNode(A[-1])
        # h = a
        # l = []
        # import heapq
        # l.append(-1*A[0])
        # heapq.heapify(l)
        # for i in range(1, len(A)):
        #     heapq.heappush(l, -1*A[i])
        # heapq.heapify(l)
        # for i in range(len(l)):
        #     l[i] = abs(l[i])
        # print(l)
        # return solve(0, l)
        # A.sort()
        # for i in range(len(A)-2, -1,-1):
        #     h.left = TreeNode(A[i])
        #     h = h.left
        # return a
            
