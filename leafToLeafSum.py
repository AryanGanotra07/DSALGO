class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def diameter(root, res):
    if root == None:
        return 0
    l = diameter(root.left, res)
    r = diameter(root.right, res)
    temp = max(l,r) + root.val
    ans = max(temp, root.val + r + l)
    res = max(ans, res)
    return temp

if __name__ == "__main__":
    root = Tree(1)
    root.left = Tree(0)
    root.right = Tree(2)
    res = 0
    print(diameter(root, res))