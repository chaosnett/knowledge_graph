from knowledge_graph.Graphs.AbstractGraphs.AbstractGraph import AbstractGraph
from knowledge_graph.Nodes.RelationshipNode import RelationshipNode
from knowledge_graph.Nodes.Node import Node

class MainNetwork(AbstractGraph):
    def __init__(self):
        super().__init__()
        self.nodes = {}
        self.edges = {}
        self.node_indices = {}
        self.adj_matrix = [[]]
    

    def add_edge(self, edge: RelationshipNode):
        if edge.id not in self.edges:
            self.edges[edge.id] = edge
            self

