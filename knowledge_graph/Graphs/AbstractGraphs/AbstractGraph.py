from abc import ABC, ABCMeta, abstractmethod
from knowledge_graph.Nodes.Node import Node
from knowledge_graph.Nodes.RelationshipNode import RelationshipNode
from knowledge_graph.Abstract_Relationships.ReificationRelationship import ReificationRelationship

class AbstractGraph(ABC):

    @abstractmethod
    def add_node(self, node: Node):
        pass

    @abstractmethod
    def add_edge(self, edge : RelationshipNode):
        pass

    @abstractmethod 
    def remove_node(self, node_id):
        pass

    @abstractmethod
    def remove_edge(self, edge_id):
        pass

    @abstractmethod
    def print_graph(self):
        pass

    
    @abstractmethod
    def build_adjacency_matrix(self):
        pass
