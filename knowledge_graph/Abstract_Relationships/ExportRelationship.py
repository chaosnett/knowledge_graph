from abc import ABC, abstractmethod
from knowledge_graph.Nodes.RelationshipNode import RelationshipNode
from knowledge_graph.Enums.relationship_types import RelationshipType
from knowledge_graph.Nodes.Node import Node

class ExportRelationship(RelationshipNode, ABC):
    def __init__(self, name : str, to_node : Node, from_node : Node):
        super().__init__(name, to_node, from_node)
        self.relationship_type = self.get_relationship_type() # product or service

    @abstractmethod
    def export_specific_method(self):
        pass

    @abstractmethod    
    def get_relationship_type(self):
        pass
