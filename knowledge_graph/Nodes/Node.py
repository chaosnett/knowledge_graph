from knowledge_graph.Enums.node_type import NodeType
from abc import ABC, abstractmethod
import uuid

class Node(ABC):
    def __init__(self, name):
        self.name = name
        self.id = uuid()
        self.node_type = self.get_node_type()

    @abstractmethod    
    def get_node_type():
        pass
    
    def __repr__(self):
        return f"{self.node_type.name}: {self.name} ID: {self.id}"
        