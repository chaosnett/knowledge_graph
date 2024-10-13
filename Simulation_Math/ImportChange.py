from knowledge_graph.Graphs.ConcreteGraphs.MainNetwork import MainNetwork
from knowledge_graph.Enums.product_types import Product
from knowledge_graph.Nodes.CountryNode import CountryNode
from knowledge_graph.Concrete_Relationships.ImportProductRelationship import ImportProductRelationship

# decrease import by %
class ImportChange:
    def __init__(self, graph: MainNetwork):
        self.graph = graph

    def decrease_import_by_percentage(self, country_name: str, product: Product, percentage: float):
        results = {}

        country_node = None
        for node in self.graph.nodes.values():
            if isinstance(node, CountryNode) and node.name == country_name:
                country_node = node
                break

        import_relationship = None
        for edge in self.graph.edges.values():
            if isinstance(edge, ImportProductRelationship) and edge.to_node == country_node and edge.product == product:
                import_relationship = edge
                break

        original_import_amount = import_relationship.amount
        original_total_imports = country_node.total_imports
        original_trade_balance = country_node.total_exports - original_total_imports

        delta_Mcp = original_import_amount * percentage
        Mcp_new = original_import_amount * (1 - percentage)

        import_relationship.amount = Mcp_new
        country_node.total_imports -= delta_Mcp
        new_total_imports = country_node.total_imports
        Bc_new = country_node.total_exports - new_total_imports
        delta_Bc = Bc_new - original_trade_balance

        results = {
            'country': country_name,
            'product': product.name,
            'original_import_value': original_import_amount,
            'new_import_value': Mcp_new,
            'change_in_import_value': -delta_Mcp,  
            'original_total_imports': original_total_imports,
            'new_total_imports': new_total_imports,
            'change_in_total_imports': -delta_Mcp,  
            'original_trade_balance': original_trade_balance,
            'new_trade_balance': Bc_new,
            'change_in_trade_balance': delta_Bc
        }

        return results
