# export_relationship.py
from abc import ABC, abstractmethod
from RelationshipNode import RelationshipNode

class ExportRelationship(RelationshipNode, ABC):
    def __init__(self, name, relationship_id, product, service):
        super().__init__(name, relationship_id)
        self.product = product
        self.service = service

    @abstractmethod
    def export_specific_method(self):
        pass
