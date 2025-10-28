# Creator : Khady Gueye

 # Creator: Khady Gueye

import tkinter as tk
from tkinter import messagebox

# Node class for circular linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Circular linked list implementation
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Create a circular list with n players
    def create(self, n):
        if n < 2:
            return
        self.head = Node(0)
        current = self.head
        for i in range(1, n):
            current.next = Node(i)
            current = current.next
        current.next = self.head  # Make the list circular

    # Eliminate every k-th player and yield eliminated players
    def eliminate(self, k):
        current = self.head
        prev = None
        while current.next != current:
            for _ in range(k - 1):
                prev = current
                current = current.next
            prev.next = current.next
            eliminated = current.data
            current = current.next
            yield eliminated
        self.head = current
        yield current.data  # Yield the winner


# GUI for the counting-out game
class CountingGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Counting Out Game")
        self.root.geometry("600x400")

        # Game state
        self.cll = None
        self.elimination_generator = None
        self.players = {}
        self.N = 0
        self.K = 0

        # Input section for N and K
        input_frame = tk.Frame(root)
        input_frame.pack(pady=10)

        # Input fields for N and K
        tk.Label(root, text="Enter N (2-11):").grid(row=0, column=0)
        self.n_entry = tk.Entry(root)
        self.n_entry.grid(row=0, column=1)

        tk.Label(root, text="Enter K (≥1):").grid(row=1, column=0)
        self.k_entry = tk.Entry(root)
        self.k_entry.grid(row=1, column=1)

        # Start button
        self.start_button = tk.Button(root, text="Start", command=self.start_game)
        self.start_button.grid(row=2, column=0, columnspan=2)

        # Text widget to show game messages
        self.text_widget = tk.Text(root, height=10, width=40)
        self.text_widget.grid(row=3, column=0, columnspan=2, pady=10)

        # Eliminate button (initially disabled)
        self.eliminate_button = tk.Button(root, text="Eliminate", command=self.eliminate_player)
        self.eliminate_button.grid(row=4, column=0, columnspan=2)
        self.eliminate_button.config(state="disabled")

        # Frame to hold player icons
        self.circle_frame = tk.Frame(root)
        self.circle_frame.grid(row=5, column=0, columnspan=2, pady=10)

    # Start a new game
    def start_game(self):
        # Validate inputs
        try:
            self.N = int(self.n_entry.get())
            self.K = int(self.k_entry.get())
        except ValueError:
            messagebox.showinfo("Invalid Input", "N and K must be integers.")
            return

        if not (1 < self.N < 12) or self.K < 1:
            messagebox.showinfo("Invalid Input", "N must be between 2-11 and K ≥ 1.")
            return

        # Set up game state
        self.cll = CircularLinkedList()
        self.cll.create(self.N)
        self.elimination_generator = self.cll.eliminate(self.K)

        # Clear previous game UI
        self.text_widget.delete('1.0', tk.END)
        for widget in self.circle_frame.winfo_children():
            widget.destroy()
        self.players.clear()

        # Display players
        for i in range(self.N):
            label = tk.Label(self.circle_frame, text=str(i), borderwidth=2, relief="groove", width=3)
            label.grid(row=0, column=i, padx=5)
            self.players[i] = label

        # Update text widget and enable elimination
        self.text_widget.insert(tk.END, f"Game started. N={self.N} K={self.K}\n")
        self.eliminate_button.config(state="normal")

    # Eliminate a player on button click
    def eliminate_player(self):
        try:
            eliminated = next(self.elimination_generator)
        except StopIteration:
            return

        # Remove player icon from UI
        if eliminated in self.players:
            self.players[eliminated].destroy()
            del self.players[eliminated]

        # If one player remains, show winner and reset
        if len(self.players) == 1:
            winner = list(self.players.keys())[0]
            messagebox.showinfo("Winner", f"The winner is Player {winner}!")
            self.text_widget.delete('1.0', tk.END)
            for widget in self.circle_frame.winfo_children():
                widget.destroy()
            self.players.clear()
            self.eliminate_button.config(state="disabled")
        else:
            self.text_widget.insert(tk.END, f"Player {eliminated} eliminated.\n")

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    app = CountingGameGUI(root)
    root.mainloop()
