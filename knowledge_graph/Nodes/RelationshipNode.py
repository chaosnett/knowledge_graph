from abc import ABC, abstractmethod, ABCMeta
from knowledge_graph.Nodes.Node import Node
from knowledge_graph.Enums.node_type import NodeType

class RelationshipNode(Node, ABCMeta):
    def __init__(self, name, to_node, from_node):
        super().__init__(name, to_node, from_node)   
        self.relationship_type = self.get_relationship_type()

    def get_node_type(self):
        return NodeType.RELATIONSHIP

    @abstractmethod    
    def get_relationship_type(self):
        pass
    
    @abstractmethod
    def relationship_details(self):
        pass