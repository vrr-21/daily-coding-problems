class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node):
    serialized_string = ""
    if node == None:
        serialized_string = "/"
    else:
        serialized_string = serialized_string + str(node.val) + ","
        serialized_string = serialized_string + serialize(node.left) + ","
        serialized_string = serialized_string + serialize(node.right)
    return serialized_string
    
if __name__ == '__main__':
    node = Node(1, Node(2), Node(3))
    print(serialize(node))
