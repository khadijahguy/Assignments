# Creator: Khady Gueye


# Define a class for an undirected graph
class UndirectedGraph:
    def __init__(self):
        # Empty dictionary to store graph
        self.adj_list = {}

    def add_edge(self, u, v):
        # If node u and v is not in the graph add it 
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        # Add v to u's neighbor list and vice versa
        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)
        if u not in self.adj_list[v]:
            self.adj_list[v].append(u)

    def node_exists(self, u):
        # Check if the node u exists 
        return u in self.adj_list

    def edge_exists(self, u, v):
        # Check if both exist and if they are neighbors
        return u in self.adj_list and v in self.adj_list[u]

    def get_neighbors(self, u):
        # Return the neighbors of node u
        if u in self.adj_list:
            return self.adj_list[u]
        # If doesn't exist
        return []

    def get_edge_density(self):
        # Get the number of nodes in the graph
        num_nodes = len(self.adj_list)
        # Less than 2 nodes edge density = 0
        if num_nodes < 2:
            return 0.0
        # Calculate
        total_possible_edges = num_nodes * (num_nodes - 1) / 2
        actual_edges = sum(len(neighbors) for neighbors in self.adj_list.values()) / 2
        # Return the edge density rounded
        return round(actual_edges / total_possible_edges, 2)

    def is_complete(self):
        # Complete if edge density is 1.0
        return self.get_edge_density() == 1.0




# Driver code 
graph = UndirectedGraph()

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 3)

# Check the outputs
print(graph.node_exists(1))     # Expected output: True

print(graph.node_exists(18))    # Expected output: False

print(graph.edge_exists(1, 2))  # Expected output: True

print(graph.edge_exists(1, 3))  # Expected output: False

print(graph.get_neighbors(1))   # Expected output: [0, 2]

print(graph.get_edge_density()) # Expected output: 0.67

print(graph.is_complete())      # Expected output: False
