# Creator : Khady Gueye

""" This program takes a min heap that inserts values as well as deletes them. """
class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        """Insert value into the heap and maintain min-heap property."""
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

    def _bubble_up(self, index):
        """Move the element at index up to restore heap property."""
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            # Swap if child is smaller than parent
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def remove(self):
        """Remove and return the smallest element (root) from the heap."""
        if not self.heap:
            return None  # Heap is empty
        if len(self.heap) == 1:
            return self.heap.pop()

        # Swap root with last element, then remove the last (smallest)
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return root

    def _bubble_down(self, index):
        """Move the element at index down to restore heap property."""
        length = len(self.heap)
        smallest = index

        while True:
            left = 2 * index + 1
            right = 2 * index + 2

            if left < length and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < length and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

    def display(self):
        """Display the current state of the heap."""
        print(self.heap)


# Example usage:
heap = MinHeap()
heap.insert(10)
heap.insert(5)
heap.insert(14)
heap.insert(9)
heap.insert(2)
heap.display()  # Expected: [2, 5, 14, 10, 9]

removed = heap.remove()
print(f"Removed element: {removed}")
heap.display()  # Expected: [5, 9, 14, 10]
