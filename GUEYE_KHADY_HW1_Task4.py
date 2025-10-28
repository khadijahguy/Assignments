# Creator : Khady Gueye

""" This prgoram simulates Round Robin CPU scheduling using a circular linked list """

class Node:
    # Define a node to represent each process with:
    # - pid: process ID
    # - burst_time: remaining CPU time needed
    # - next: pointer to the next node in the circular list
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time
        self.next = None

class CircularLinkedList:
    def __init__(self):
        # Initialize an empty circular linked list with no head node
        self.head = None

    def append(self, pid, burst_time):
        # Create a new node for the process
        new_node = Node(pid, burst_time)
        if not self.head:
            # If list is empty, new node points to itself and becomes head
            self.head = new_node
            new_node.next = new_node
            return
        # Otherwise, find the last node in the circular list
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        # Append the new node after last and close the circle
        temp.next = new_node
        new_node.next = self.head

    def remove(self, node):
        # Remove the given node from the circular list
        if node == node.next:
            # If only one node, list becomes empty
            self.head = None
            return
        # Find the node before the one to remove
        prev = node
        while prev.next != node:
            prev = prev.next
        # Bypass the node to remove it
        prev.next = node.next
        # If the node removed is head, update head pointer
        if self.head == node:
            self.head = node.next

    def is_empty(self):
        # Check if the circular list is empty
        return self.head is None

    def display(self):
        # Print all processes and their remaining burst times
        if self.is_empty():
            print("No processes.")
            return
        temp = self.head
        seen = set()
        print("Processes in the list:")
        # Traverse nodes until full circle is completed
        while temp and temp not in seen:
            print(f"Process {temp.pid}: Remaining Burst Time = {temp.burst_time}")
            seen.add(temp)
            temp = temp.next

def round_robin_scheduler(processes, quantum):
    cll = CircularLinkedList()
    # Add all processes into the circular linked list
    for pid, bt in processes:
        cll.append(pid, bt)

    print("Initial Process List:")
    cll.display()

    print("\nStarting Round Robin Scheduling:")
    current = cll.head
    time_elapsed = 0

    # Run scheduling until no processes remain
    while not cll.is_empty():
        print(f"Time: {time_elapsed}, Processing PID: {current.pid}")
        if current.burst_time <= quantum:
            # If process can finish in this quantum
            time_elapsed += current.burst_time
            print(f"Process {current.pid} completed.")
            next_node = current.next
            cll.remove(current)  # Remove finished process
            if cll.is_empty():
                break
            current = next_node  # Move to next process
        else:
            # Process uses full quantum, update burst time and time elapsed
            current.burst_time -= quantum
            time_elapsed += quantum
            print(f"Process {current.pid} now has {current.burst_time} units remaining.")
            current = current.next  # Move to next process

    print("All processes completed.")

if __name__ == "__main__":
    # Sample input: list of (Process ID, Burst Time) and quantum
    processes = [(1, 10), (2, 5), (3, 8)]
    quantum_time = 4
    # Start the scheduler
    round_robin_scheduler(processes, quantum_time)
