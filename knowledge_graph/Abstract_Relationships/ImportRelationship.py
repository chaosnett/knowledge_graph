from abc import ABC, abstractmethod
from knowledge_graph.Nodes.RelationshipNode import RelationshipNode
from knowledge_graph.Nodes.Node import Node
from knowledge_graph.Enums.product_types import Product

class ImportRelationship(RelationshipNode, ABC):
    def __init__(self, name : str, to_node : Node, from_node : Node, product : Product, amount : float):
        super().__init__(name, to_node, from_node)
        self.relationship_type = self.get_relationship_type() # product or service
        self.product = product
        self.amount = amount
        
    @abstractmethod    
    def get_relationship_type(self):
        pass

    