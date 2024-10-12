from abc import ABC, abstractmethod
from RelationshipNode import RelationshipNode

class ImportRelationship(RelationshipNode, ABC):
    def __init__(self, name, to_node, from_node):
        super().__init__(name, to_node, from_node)
        
    
    @abstractmethod
    def import_product_or_service(self):
        pass
