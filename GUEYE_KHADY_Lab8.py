# Creator: Khady Gueye

""" This program recursively evaluates a binary parse tree to comput a math expresion"""

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Construct the parse tree for ((7 + 3) * (5 - 2))
root = Node('*')
root.left = Node('+', Node(7), Node(3))
root.right = Node('-', Node(5), Node(2))

def evaluate(node):
    # Base case: if the node is a number (leaf node)
    if node.left is None and node.right is None:
        return float(node.value)  # convert to float for division

    # Recursively evaluate the left and right subtrees
    left_val = evaluate(node.left)
    right_val = evaluate(node.right)

    # Apply the operator
    if node.value == '+':
        return left_val + right_val
    elif node.value == '-':
        return left_val - right_val
    elif node.value == '*':
        return left_val * right_val
    elif node.value == '/':
        return left_val / right_val
    else:
        raise ValueError(f"Unknown operator: {node.value}")

# Test
print(evaluate(root))  # Should print 30.0
