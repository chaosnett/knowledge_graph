from RelationshipNode import RelationshipNode

class ExportProductRelationship(RelationshipNode):
    def __init__(self, name, relationship_id, product, to_country, from_country):
        super().__init__(name, relationship_id)
        self.product = product  
        self.to_country = to_country   
        self.from_country = from_country

    def relationship_details(self):
        return f"Exporting from {self.from_country} to {self.to_country}"

    def process_export(self):
        print(f"Exporting product: {self.product}")
