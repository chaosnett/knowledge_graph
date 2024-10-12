from Node import Node
from node_type import NodeType

class CountryNode(Node):
    def __init__(self, name, country_id):
        super().__init__(name, country_id)

    def get_node_type(self):
        return NodeType.COUNTRY

