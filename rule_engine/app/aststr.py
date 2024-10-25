#Creating a Node representing AST(Abstract syntax tree) consisting of node with its left and right childs with value

class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type  # 'operator' or 'operand'
        self.left = left  # left child
        self.right = right  # right child
        self.value = value  # value 

    def __repr__(self):
        return f"Node({self.node_type}, {self.value}, {self.left}, {self.right})"