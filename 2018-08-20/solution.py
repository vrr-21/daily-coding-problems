class tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def getVal(root):
    if root.left == None and root.right == None:
        return root.val
    else:
        x = getVal(root.left)
        y = getVal(root.right)
        if root.val == "*":
            return x*y
        elif root.val == "+":
            return x+y
        elif root.val == "-":
            return x-y
        else:
            return x//y


if __name__ == '__main__':
    root = tree("*")
    root.left = tree("+")
    root.left.left = tree(3)
    root.left.right = tree(2)
    root.right = tree("+")
    root.right.left = tree(4)
    root.right.right = tree(5)
    print(getVal(root))