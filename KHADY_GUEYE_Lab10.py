class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Build the sample tree
grand_child1 = TreeNode(4)
grand_child2 = TreeNode(5)
child1 = TreeNode(9, grand_child1, grand_child2)
child2 = TreeNode(8)
parent = TreeNode(3, child1, child2)


# Traverse the tree - Pre-order traversal (Root -> Left -> Right)
def traversePreOrder(node):
    if node is None:
        return
    
    # Print the value of the current node
    print(node.value, end=" ")

    # Recur on left and right subtrees
    traversePreOrder(node.left)
    traversePreOrder(node.right)


# Trim the entire tree (decrease all node values by 1)
def trim(node):
    if node is None:
        return
    
    node.value -= 1  
    trim(node.left)
    trim(node.right)


# Trim only the leaves (decrease leaf node values by 1)
def trim_leaves(node):
    if node is None:
        return
    
    if node.left is None and node.right is None:
        node.value -= 1
        return
    
    trim_leaves(node.left)
    trim_leaves(node.right)


# Mirror the tree (swap left and right subtrees)
def mirror(node):
    if node is None:
        return
    
    node.left, node.right = node.right, node.left
    mirror(node.left)
    mirror(node.right)


# Run the tests
print('Original tree:')
traversePreOrder(parent)

print('\nAfter trimming entire tree:')
trim(parent)
traversePreOrder(parent)

print('\nAfter trimming only the leaves:')
trim_leaves(parent)
traversePreOrder(parent)

print('\nAfter mirroring the tree:')
mirror(parent)
traversePreOrder(parent)