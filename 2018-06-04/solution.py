class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return self.val+"L"+str(self.left)+"R"+str(self.right)

def serialize(node):
    serialized_string = ""
    if node == None:
        serialized_string = "/"
    else:
        serialized_string = serialized_string + str(node.val) + ","
        serialized_string = serialized_string + serialize(node.left) + ","
        serialized_string = serialized_string + serialize(node.right)
    return serialized_string

def deserialize(s):
    vals_list = s.split(",")
    root = Node(vals_list[0])
    del vals_list[0]
    nodes_stack = [root]
    iteration = 0
    while len(nodes_stack) > 0:
        considered_node = nodes_stack[-1]
        # Getting the left side:
        if considered_node.left == None:
            while len(vals_list) > 0 and vals_list[0] != '/':
                temp_node = Node(vals_list[0])
                del vals_list[0]
                considered_node.left = temp_node
                nodes_stack.append(temp_node)
                considered_node = temp_node
            # Removing the /
            if len(vals_list) > 0:
                del vals_list[0]
        # Getting the right side:
        if considered_node.right == None:
            while len(vals_list) > 0 and vals_list[0] != '/':
                temp_node = Node(vals_list[0])
                del vals_list[0]
                considered_node.right = temp_node
                nodes_stack.append(temp_node)
                considered_node = temp_node
            if len(vals_list) > 0:
                del vals_list[0]
        iteration = iteration + 1 
        nodes_stack.pop()
    return root
    
if __name__ == '__main__':
    node = Node(1, Node(2), Node(3))
    print(serialize(node))
    # node = Node(1, Node(3, Node(4)), Node(2))
    # serialized = serialize(node)
    # recons_tree = deserialize(serialized)
    # print(recons_tree)
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
