from abc import ABC, abstractmethod, ABCMeta
from knowledge_graph.Nodes.Node import Node
from knowledge_graph.Enums.node_type import NodeType
import uuid

class RelationshipNode(ABC):
    def __init__(self, name, to_node : Node, from_node : Node):
        self.name = name
        self.id = uuid.uuid4()
        self.relationship_type = self.get_relationship_type()
        self.to_node = to_node
        self.from_node = from_node

    def get_node_type(self):
        return NodeType.RELATIONSHIP

    @abstractmethod    
    def get_relationship_type(self):
        pass
    


#ReificationRelationshipNode --> child of RelationShipNode
# 