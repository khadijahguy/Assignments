# Crdeator Khady Gueye

""" This program concatenates two singly linked lists by attaching the shorter list first then the longer list."""

# Node class for singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to concatenate two linked lists
def concatenate(h1, h2, len1, len2):
    # If list1 is shorter → list1 + list2
    if len1 < len2:
        head = h1
        tail = h1
        while tail.next:
            tail = tail.next
        tail.next = h2
    else:
        head = h2
        tail = h2
        while tail.next:
            tail = tail.next
        tail.next = h1
    return head

# Utility function: create linked list from Python list
def create_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for v in values[1:]:
        current.next = Node(v)
        current = current.next
    return head

# Utility function: print linked list
def print_list(head):
    current = head
    while current:
        print(current.data, end=" → " if current.next else "")
        current = current.next
    print()

# ---------------- Driver Code ----------------
# Test Case #1
list1 = create_linked_list([3,4,5])
list2 = create_linked_list([1,2])
result = concatenate(list1, list2, 3, 2)
print("Case #1 Result:")
print_list(result)   # Expected: 1 → 2 → 3 → 4 → 5

# Test Case #2
list1 = create_linked_list([4,5])
list2 = create_linked_list([1,2,3])
result = concatenate(list1, list2, 2, 3)
print("Case #2 Result:")
print_list(result)   # Expected: 4 → 5 → 1 → 2 → 3