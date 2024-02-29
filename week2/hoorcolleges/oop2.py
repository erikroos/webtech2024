class Animal:
    name = "Animal"

    def drink(self):
        print("Drinking some fluid")

    def make_noise(self):
        print("Some general animal noise")

class Duck(Animal):
    name = "Duck"

    def make_noise(self):
        print(f"{Duck.name}: Quack")

class Penguin(Animal):
    name = "Penguin"

    def make_noise(self):
        print(f"{Penguin.name}: I don't know what noise to make!")
        super().make_noise()

class Horse(Animal):
    name = "Horse"

    def drink(self):
        print("Drinking water")

    def make_noise(self):
        print(f"{self.name}: Wheeheehee")

class Pony(Horse):
    name = "Pony"


henk = Horse()
peter = Pony()
donald = Duck()
percy = Penguin()


animals = [donald, percy, henk, peter]

for animal in animals:
    animal.make_noise()
    animal.drink()
    print()