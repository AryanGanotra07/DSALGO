class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self, root):
        self.root = root
    
    def insert(self,root, node):
        if node is None or root is None:
            return 
        if node.val < root.val:
            if root.left is None:
                root.left = node 
                return 
            self.insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
                return 
            self.insert(root.right, node)
    
    def search(self, root, node):
        if root is None:
            return False
        if node is None:
            return True
        if root.val == node.val:
            return True
        if root.val > node.val:
            return self.search(root.left, node)
        else:
           return self.search(root.right, node)

    def __minValNode(self, node):
        current = node
        while(current.left is not None):
            current = current.left
        return current

    def delete(self, root, node):
        if root is None:
            return root
        if root.val > node.val:
            root.left = self.delete(root.left, node)
        elif root.val < node.val:
            root.right = self.delete(root.right, node)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.__minValNode(root.right)
            root.val = temp.val 
            root.right = self.delete(root.right, temp)
        return root
        
        
    def inorder(self, root):
        if root is None:
            return 
        self.inorder(root.left)
        print(root.val, end = " ")
        self.inorder(root.right)

        
        
        
root = Node(10)
root.left = Node(8)
root.right = Node(12)
tree = BST(root)
tree.inorder(root)
print(tree.search(root, Node(12)))
tree.insert(root, Node(4))
tree.inorder(root)
print()
tree.delete(root, Node(4))
tree.inorder(root)
    