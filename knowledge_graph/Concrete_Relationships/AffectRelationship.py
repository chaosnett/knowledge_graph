from knowledge_graph.Abstract_Relationships.ReificationRelationship import ReificationRelationship
from knowledge_graph.Enums.relationship_types import RelationshipType
from knowledge_graph.Nodes.Node import Node

class AffectRelationship(ReificationRelationship):
    def __init__(self, name : str, to_node : Node, from_node : Node, formula_fn : function):
        super().__init__(name, to_node, from_node)
        self.formula_fn = formula_fn

    def get_relationship_type(self) -> RelationshipType:
        return RelationshipType.PRODUCT
    
    def base_formula(self) -> float:
        return self.formula_fn() 
