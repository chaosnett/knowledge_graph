from knowledge_graph.Abstract_Relationships.ImportRelationship import ImportRelationship
from knowledge_graph.Enums.relationship_types import RelationshipType
from knowledge_graph.Nodes.Node import Node


class ImportProductRelationship(ImportRelationship):
    def __init__(self, name: str, to_node : Node, from_node : Node):
        super().__init__(name, to_node, from_node)

    def get_relationship_type(self) -> RelationshipType:
        return RelationshipType.PRODUCT