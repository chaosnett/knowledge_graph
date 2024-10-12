from ImportRelationship import ImportRelationship

class ImportProductRelationship(ImportRelationship):
    def __init__(self, name, relationship_id, product, to_country, from_country):
        super().__init__(name, relationship_id)
        self.product = product
        self.to_country = to_country
        self.from_country = from_country

    def import_details(self):
        return f"importing {self.product} from {self.from_country} to {self.to_country}"

    def import_product_or_service(self):
        print(f"importing {self.poduct}")
        return super().import_product()
