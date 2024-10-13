from knowledge_graph.Graphs.ConcreteGraphs.MainNetwork import MainNetwork
from knowledge_graph.Enums.product_types import Product
from knowledge_graph.Nodes.CountryNode import CountryNode
from knowledge_graph.Concrete_Relationships.ImportProductRelationship import ImportProductRelationship

class TariffChange:
    def __init__(self, Mc, Xc, Mcp, Xcp, Tcp, graph : MainNetwork):
        self.Mc = Mc    # Total imports value for country c
        self.Xc = Xc    # Total exports value for country c
        self.Mcp = Mcp  # Import value of product p
        self.Xcp = Xcp  # Export value of product p
        self.Tcp = Tcp  # Original tariff rate on product p
        self.graph = graph

    # apply import tarrif to all relations for a country with product, and apply tarrif and 
    # update countries total imports && trade balance
    def apply_tariff_change(self, country_name: str, product: Product, delta_tariff: float):
        country_node = None
        for node in self.graph.nodes.values():
            if isinstance(node, CountryNode) and node.name == country_name:
                country_node = node
                break
        if not country_node:
            print(f"Country '{country_name}' not found in the graph.")
            return
        affected_relationships = []
        
        for edge in self.graph.edges.values():
            if isinstance(edge, ImportProductRelationship):
                if edge.to_node == country_node and edge.product == product:
                    affected_relationships.append(edge)

        for relationship in affected_relationships:
            self._update_import_relationship(relationship, delta_tariff)

        self._update_country_trade_balance(country_node)


    # calculate new tarrif rate & updates it
    # adjusts tarrif value with import quantity 
    def _update_import_relationship(self, relationship: ImportProductRelationship, delta_tariff: float):
        original_tariff = relationship.tariff_rate
        new_tariff = original_tariff + delta_tariff

        original_import_value = relationship.amount
        new_import_value = original_import_value * (1 - delta_tariff / (1 + original_tariff))

        original_tariff_revenue = original_tariff * original_import_value
        new_tariff_revenue = new_tariff * new_import_value

        relationship.tariff_rate = new_tariff
        relationship.amount = new_import_value
        relationship.original_tariff_revenue = original_tariff_revenue
        relationship.new_tariff_revenue = new_tariff_revenue

    def _update_country_trade_balance(self, country_node: CountryNode):
        total_imports = 0.0
        total_exports = country_node.total_exports  

        for edge in self.graph.edges.values():
            if isinstance(edge, ImportProductRelationship) and edge.to_node == country_node:
                total_imports += edge.amount

        country_node.total_imports = total_imports
        trade_balance = total_exports - total_imports

        print(f"Updated Country Trade Balance for {country_node.name}:")
        print(f"  Total Imports: {total_imports}")
        print(f"  Total Exports: {total_exports}")
        print(f"  Trade Balance: {trade_balance}\n")

    def calculate_new_tariff_rate(self, delta_Tcp):
        self.delta_Tcp = delta_Tcp
        self.Tcp_new = self.Tcp + self.delta_Tcp
        return self.Tcp_new

    # Assume a small change in import value due to tariff change
    def calculate_new_import_value(self):
        self.Mcp_new = self.Mcp * (1 - self.delta_Tcp / (1 + self.Tcp))
        return self.Mcp_new

    # New total imports after change
    def calculate_new_total_imports(self):
        self.Mc_new = self.Mc - (self.Mcp - self.Mcp_new)
        return self.Mc_new

    def calculate_change_in_trade_balance(self):
        self.Bc = self.Xc - self.Mc
        self.Bc_new = self.Xc - self.Mc_new

        # Change in trade balance
        self.delta_Bc = self.Bc_new - self.Bc
        return self.delta_Bc
        
    def calculate_original_tariff_revenue(self):
        self.Rcp = self.Tcp * self.Mcp
        return self.Rcp

    def calculate_new_tariff_revenue(self):
        self.Rcp_new = self.Tcp_new * self.Mcp_new
        return self.Rcp_new

    def calculate_change_in_tariff_revenue(self):
        self.delta_Rcp = self.Rcp_new - self.Rcp
        return self.delta_Rcp

    def calculate_total_tariff_revenue(self):
        self.Rc = self.Rcp
        self.Rc_new = self.Rcp_new
        self.delta_Rc = self.Rc_new - self.Rc
        return self.delta_Rc
