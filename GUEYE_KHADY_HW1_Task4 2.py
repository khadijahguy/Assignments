# Creator : Khady Gueye

""" """

class Node:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, pid, burst_time):
        new_node = Node(pid, burst_time)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    def remove(self, node):
        if node == node.next:
            self.head = None
            return
        prev = node
        while prev.next != node:
            prev = prev.next
        prev.next = node.next
        if self.head == node:
            self.head = node.next

    def is_empty(self):
        return self.head is None

    def display(self):
        if self.is_empty():
            print("No processes.")
            return
        temp = self.head
        seen = set()
        print("Processes in the list:")
        while temp and temp not in seen:
            print(f"Process {temp.pid}: Remaining Burst Time = {temp.burst_time}")
            seen.add(temp)
            temp = temp.next

def round_robin_scheduler(processes, quantum):
    cll = CircularLinkedList()
    for pid, bt in processes:
        cll.append(pid, bt)

    print("Initial Process List:")
    cll.display()

    print("\nStarting Round Robin Scheduling:")
    current = cll.head
    time_elapsed = 0
    while not cll.is_empty():
        print(f"Time: {time_elapsed}, Processing PID: {current.pid}")
        if current.burst_time <= quantum:
            time_elapsed += current.burst_time
            print(f"Process {current.pid} completed.")
            next_node = current.next
            cll.remove(current)
            if cll.is_empty():
                break
            current = next_node
        else:
            current.burst_time -= quantum
            time_elapsed += quantum
            print(f"Process {current.pid} now has {current.burst_time} units remaining.")
            current = current.next

    print(f"All processes completed.")

# Driver Code
if __name__ == "__main__":
    processes = [(1, 10), (2, 5), (3, 8)]
    quantum_time = 4
    round_robin_scheduler(processes, quantum_time)
