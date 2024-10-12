from Node import Node
from node_type import NodeType

class IndustryNode(Node):
    def __init__(self, name, industry_id):
        super().__init__(name, industry_id)

    def get_node_type(self):
        return NodeType.INDUSTRY