from abc import ABC, abstractmethod, ABCMeta
from Node import Node
from node_type import NodeType

# parent of import/export rel node
# classes: import/export have the actual 
class RelationshipNode(Node, metaclass=ABCMeta):
    def __init__(self, name, to_node, from_node):
        super().__init__(name, to_node, from_node)   

    def get_node_type(self):
        return NodeType.RELATIONSHIP
    
    @abstractmethod
    def relationship_details():
        pass