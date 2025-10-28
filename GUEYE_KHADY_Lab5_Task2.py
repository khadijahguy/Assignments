# Creator: Khady Gueye


""" This program finds the length of a doubly linked list. """

# Node class for doubly linked list
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Function to find length of doubly linked list from any node
def findLength(node):
    if not node:
        return 0

    # Step 1: Go backward to find the head
    head = node
    while head.prev:
        head = head.prev

    # Step 2: Traverse forward to count
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    return length

# Utility function: create doubly linked list
def create_doubly_linked_list(values):
    if not values:
        return None
    head = DoublyNode(values[0])
    current = head
    for v in values[1:]:
        new_node = DoublyNode(v)
        current.next = new_node
        new_node.prev = current
        current = new_node
    return head

# ---------------- Driver Code ----------------
dlist = create_doubly_linked_list([10, 20, 30, 40])
mid_node = dlist.next.next   # Node with value 30
print("Length of doubly linked list:", findLength(mid_node))  # Expected: 4