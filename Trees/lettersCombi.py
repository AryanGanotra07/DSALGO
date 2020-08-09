# Data structure to store a Binary Tree node
class Node:
    # Constructor
    def __init__(self, key="", left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
 
 
# Function to print all leaf nodes of the binary tree
def printBT(node):
    if node is None:
        return
 
    if node.left is None and node.right is None:
        print(node.key, end=' ')
    else:
        printBT(node.right)
        printBT(node.left)
 
 
# Function to construct a binary tree where each leaf node contains
# one unique combination of words formed
def construct(root, alphabet, digit, i):
    # Base case: empty tree
    if root is None or i == len(digit):
        return
 
    # check if digit[i+1] exists
    if i + 1 < len(digit):
 
        # process current and next digit
        sum = 10 * digit[i] + digit[i + 1]
 
        # if a valid character can be formed by both digits
        # create left child from it
        if sum <= 26:
            root.left = Node(root.key + alphabet[sum - 1])
 
        # construct left subtree by remaining digits
        construct(root.left, alphabet, digit, i + 2)
 
    # process current digit and create right child from it
    root.right = Node(root.key + alphabet[digit[i] - 1])
 
    # construct right subtree by remaining digits
    construct(root.right, alphabet, digit, i + 1)
 
 
if __name__ == '__main__':
 
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digit = [1, 2, 2, 1]
 
    # create an empty root
    root = Node()
 
    # construct binary tree
    construct(root, alphabet, digit, 0)
 
    printBT(root)