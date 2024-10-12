from knowledge_graph.Graphs.ConcreteGraphs.MainNetwork import MainNetwork
from knowledge_graph.Nodes.IndustryNode import IndustryNode
from knowledge_graph.Nodes.CountryNode import CountryNode
from knowledge_graph.Nodes.RelationshipNode import RelationshipNode
from knowledge_graph.Concrete_Relationships.ExportProductRelationship import ExportProductRelationship
from knowledge_graph.Nodes.CountryNode import CountryNode
from knowledge_graph.Enums.product_types import Product


def main():
    graph = MainNetwork()
    
    usa = CountryNode("USA")
    china = CountryNode("China")
    tech_industry = IndustryNode("Technology")

    graph.add_node(usa)
    graph.add_node(china)
    graph.add_node(tech_industry)

    export_rel = ExportProductRelationship(
        name="China Exports Electronics to USA",
        from_node=china,
        to_node=usa,
        product=Product.GAS,
        amount=123
    )

    industry_rel = ExportProductRelationship(
    name="USA Exports Software to Technology Industry",
    from_node=usa,
    to_node=tech_industry,
    product=Product.GAS,
    amount=1234
    )

    graph.add_edge(export_rel)
    graph.add_edge(industry_rel)

    # graph.print_graph()
    graph.display_adjacency_matrix()

if __name__ == "__main__":
    main()