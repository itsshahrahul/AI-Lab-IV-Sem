class Node:
    def __init__(self, name):
        self.name = name
        self.relationship = {}

    def add_relationship(self, relationship):
        self.relationship.update(relationship)

    def get_relationship(self, level=0):
        indent = ' ' * level
        print(f"{indent}{self.name}")
        for relation, node in self.relationship.items():
            if isinstance(node, Node):
                print(f"{indent}  {relation} ->", end=" ")
                node.get_relationship(level + 1)
            else:
                print(f"{indent}  {relation} -> {node}")

lion = Node('lion')
tiger = Node('tiger')
cheetah = Node('cheetah')
leopard = Node('leopard')

carnivora = Node('carnivora')
herbivore = Node('herbivore')
omnivore = Node('omnivore')
savanna = Node('savanna')
grassland = Node('grassland')
forest = Node('forest')

lion.add_relationship({'is a': carnivora, 'lives in': savanna})
tiger.add_relationship({'is a': carnivora, 'lives in': forest})
cheetah.add_relationship({'is a': carnivora, 'lives in': grassland})
leopard.add_relationship({'is a': carnivora, 'lives in': savanna})

carnivora.add_relationship({'has': 'teeth'})
carnivora.add_relationship({'has': 'claws'})
herbivore.add_relationship({'has': 'hooves'})
herbivore.add_relationship({'has': 'horns'})
omnivore.add_relationship({'has': 'teeth'})
omnivore.add_relationship({'has': 'claws'})
omnivore.add_relationship({'has': 'hooves'})
savanna.add_relationship({'is': 'hot'})
savanna.add_relationship({'is': 'dry'})
grassland.add_relationship({'is': 'wet'})
grassland.add_relationship({'is': 'green'})
forest.add_relationship({'is': 'humid'})
forest.add_relationship({'is': 'dense'})

print("Semantic Network:")

lion.get_relationship()
tiger.get_relationship()
cheetah.get_relationship()
leopard.get_relationship()
carnivora.get_relationship()
herbivore.get_relationship()
omnivore.get_relationship()
savanna.get_relationship()
grassland.get_relationship()
forest.get_relationship()
