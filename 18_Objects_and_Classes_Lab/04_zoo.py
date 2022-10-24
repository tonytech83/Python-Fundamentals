class Zoo:
    # private attribute for our class, should not be accessed outside ot the class
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    # method to take the value of private attribute __animals and print at the end
    def get_animal_count(self):
        return self.__animals

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

        self.__animals += 1

    def get_info(self, species):
        if species == 'mammal':
            # also the lists can be accessed with self.mammals / self.fishes / self.birds
            return f'Mammals in {self.name}: {", ".join(zoo.mammals)}'
        elif species == 'fish':
            return f'Fishes in {self.name}: {", ".join(zoo.fishes)}'
        elif species == 'bird':
            return f'Birds in {self.name}: {", ".join(zoo.birds)}'


zoo_name = input()
animals_count = int(input())

# create instance with name of the zoo garden
zoo = Zoo(zoo_name)

for _ in range(animals_count):
    specie, name = input().split()
    zoo.add_animal(specie, name)

searched_specie = input()

print(zoo.get_info(searched_specie))
print(f'Total animals: {zoo.get_animal_count()}')
