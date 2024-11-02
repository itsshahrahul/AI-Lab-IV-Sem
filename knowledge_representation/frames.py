class Animal:
    def __init__ (self, name, species, color):
        self.name = name
        self.species = species
        self.color = color

    def display_info(self):
        print(f"{self.name} is a {self.color} {self.species}")

def main():
    dog = Animal("Rover", "dog", "brown")
    dog.display_info()

if __name__ == "__main__":
    main()