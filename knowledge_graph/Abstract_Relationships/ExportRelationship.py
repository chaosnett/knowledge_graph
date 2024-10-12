from abc import ABC, abstractmethod
from knowledge_graph.Nodes.RelationshipNode import RelationshipNode

class ExportRelationship(RelationshipNode, ABC):
    def __init__(self, name):
        super().__init__(name)
        self.relationship_type = self.get_relationship_type() # product or service

    @abstractmethod
    def export_specific_method(self):
        pass

    @abstractmethod    
    def get_relationship_type():
        pass
