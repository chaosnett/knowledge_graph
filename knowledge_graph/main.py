from knowledge_graph.Nodes.CountryNode import CountryNode
from knowledge_graph.Nodes.IndustryNode import IndustryNode

def main():
    c = CountryNode("USA", 1)
    i = IndustryNode("retail", 3000)
    print(c, i)



if __name__ == "__main__":
    main()