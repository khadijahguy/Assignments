# Creator: Khady Gueye

""" Task 1 """
print("*** TASK 1 ***")
# The node class for circular linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def one_potato_game(n, k):
    # Create circular linked list
    head = Node(0)
    current = head
    for i in range(1, n):
        current.next = Node(i)
        current = current.next
    current.next = head  

    while current.next != head:
        current = current.next

    # Start elimination process
    while current.next != current:
        for _ in range(k - 1):
            current = current.next
        current.next = current.next.next

    # Return the value of the remaining node
    return current.value

# Example 
print(one_potato_game(11, 8)) 


# Seperator for task 1 and 2
print(" ")
print(" ")

""" Task 2 """
print("*** TASK 2 ***")
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def tree_info(node):
    # Calculate height of a tree
    def height(n):
        if not n:
            return -1
        return 1 + max(height(n.left), height(n.right))

    # Count leaf nodes
    def count_leaves(n):
        if not n:
            return 0
        if not n.left and not n.right:
            return 1
        return count_leaves(n.left) + count_leaves(n.right)

    # Check if the tree is full
    def is_full(n):
        if not n:
            return True
        if (n.left and not n.right) or (not n.left and n.right):
            return False
        return is_full(n.left) and is_full(n.right)

    # Check if the tree is balanced
    def is_balanced(n):
        if not n:
            return True
        left_height = height(n.left)
        right_height = height(n.right)
        if abs(left_height - right_height) > 1:
            return False
        return is_balanced(n.left) and is_balanced(n.right)

    # Print
    print("Height of the tree:", height(node))
    print("Number of leaf nodes:", count_leaves(node))
    print("Is Full:", "Yes" if is_full(node) else "No")
    print("Is Balanced:", "Yes" if is_balanced(node) else "No")

# Example 
root = TreeNode(1,
        TreeNode(2,
            TreeNode(4),
            TreeNode(5)),
        TreeNode(3)
    )

tree_info(root)