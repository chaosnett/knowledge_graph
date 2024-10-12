from CountryNode import CountryNode
from IndustryNode import IndustryNode
from RelationshipNode import RelationshipNode

def main():
    c = CountryNode("USA", 1)
    i = IndustryNode("retail", 3000)
    print(c, i)



if __name__ == "__main__":
    main()