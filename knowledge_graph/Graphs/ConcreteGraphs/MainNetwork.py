from knowledge_graph.Graphs.AbstractGraphs.AbstractGraph import AbstractGraph
from knowledge_graph.Nodes.RelationshipNode import RelationshipNode
from knowledge_graph.Nodes.Node import Node

class MainNetwork(AbstractGraph):
    def __init__(self):
        super().__init__()
        self.nodes = {}
        self.edges = {}
        self.node_indices = {}
        self.adjacency_matrix = [[]]
        self.next_index = 0

    def add_node(self, node: Node):
        if node.id not in self.nodes:
            self.nodes[node.id] = node
            self.node_indices[node.id] = self.next_index
            self.next_index += 1
            self._expand_adjacency_matrix()
            print(f"Node added: {node}")
        else:
            print(f"Node {node.id} already exists.")

    def add_edge(self, edge: RelationshipNode):
        if edge.id not in self.edges:
            self.edges[edge.id] = edge
            self._update_adjacency_matrix(edge)
            print(f"Edge added: {edge}")
        else:
            print(f"Edge {edge.id} already exists.")

    def remove_node(self, node_id):
        if node_id in self.nodes:
            del self.nodes[node_id]
            index = self.node_indices.pop(node_id)
            self._remove_node_from_matrix(index)
            self.next_index -= 1
            print(f"Node removed: {node_id}")
        else:
            print(f"Node {node_id} does not exist.")

    def remove_edge(self, edge_id):
        if edge_id in self.edges:
            edge = self.edges.pop(edge_id)
            self._remove_edge_from_matrix(edge)
            print(f"Edge removed: {edge_id}")
        else:
            print(f"Edge {edge_id} does not exist.")

    def build_adjacency_matrix(self):
        size = len(self.nodes)
        self.adjacency_matrix = [[0 for _ in range(size)] for _ in range(size)]
        for edge in self.edges.values():
            self._update_adjacency_matrix(edge)

    def display_adjacency_matrix(self):
        size = len(self.nodes)
        if size == 0:
            print("The graph is empty.")
            return

        index_to_node_id = {index: node_id for node_id, index in self.node_indices.items()}
        node_names = [self.nodes[index_to_node_id[i]].name for i in range(size)]

        print("\nAdjacency Matrix:")
        header = "    " + "  ".join(f"{name:>10}" for name in node_names)
        print(header)
        for i in range(size):
            row = f"{node_names[i]:>10} "
            for j in range(size):
                row += f"{self.adjacency_matrix[i][j]:>10} "
            print(row)
        print()

    def _expand_adjacency_matrix(self):
        for row in self.adjacency_matrix:
            row.append(0)
        self.adjacency_matrix.append([0 for _ in range(self.next_index)])

    def _update_adjacency_matrix(self, edge: RelationshipNode):
        from_index = self.node_indices[edge.from_node.id]
        to_index = self.node_indices[edge.to_node.id]
        self.adjacency_matrix[from_index][to_index] = 1


    def _remove_node_from_matrix(self, index):
        self.adjacency_matrix.pop(index)
        for row in self.adjacency_matrix:
            row.pop(index)
        for node_id, idx in self.node_indices.items():
            if idx > index:
                self.node_indices[node_id] = idx - 1

    def _remove_edge_from_matrix(self, edge: RelationshipNode):
        from_index = self.node_indices[edge.from_node.id]
        to_index = self.node_indices[edge.to_node.id]
        self.adjacency_matrix[from_index][to_index] = 0
    
    def print_graph(self):
        print("Nodes:")
        for node_id, node in self.nodes.items():
            print(f"  {node_id}: {node}")

        print("\nEdges:")
        for edge_id, edge in self.edges.items():
            print(f"  {edge_id}: {edge}")

        self.print_graph()