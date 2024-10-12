from knowledge_graph.Nodes.Node import Node
from knowledge_graph.Enums.node_type import NodeType

class IndustryNode(Node):
    def __init__(self, name):
        super().__init__(name)

    def get_node_type(self):
        return NodeType.INDUSTRY