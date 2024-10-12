import_service_relationship.py
from RelationshipNode import RelationshipNode

class ImportServiceRelationship(RelationshipNode):
    def __init__(self, name, service, to_node, from_node):
        super().__init__(name, to_node, from_node)
        self.service = service
    
    def import_details(self):
        return f"importing {self.service} from {self.from_node} to {self.to_node}"

    def import_product_or_service(self):
        print(f"importing {self.service}")
        return super().import_product_or_service()
