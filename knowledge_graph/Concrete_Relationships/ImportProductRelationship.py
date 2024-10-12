from knowledge_graph.Abstract_Relationships.ImportRelationship import ImportRelationship
from knowledge_graph.Enums.relationship_types import RelationshipType
from knowledge_graph.Nodes.Node import Node
from knowledge_graph.Enums.product_types import Product


class ImportProductRelationship(ImportRelationship):
    def __init__(self, name: str, to_node : Node, from_node : Node, product : Product, amount : float):
        super().__init__(name, to_node, from_node, product, amount)

    def get_relationship_type(self) -> RelationshipType:
        return RelationshipType.PRODUCT