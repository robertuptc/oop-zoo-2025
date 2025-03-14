class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def speak(self):
        return "Animal sound"

class Mammal(Animal):
    def give_birth(self):
        return f"{self.name} the {self.species} has given birth"

class Bird(Animal):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        self.wingspan = wingspan

class Reptile(Animal):
    def bask_in_sun(self):
        return f"{self.name} the {self.species} is basking in the sun"

class Primate(Animal):
    def climb_trees(self):
        return f"{self.name} the {self.species} is climbing trees"

class Marsupial(Animal):
    def carry_baby(self):
        return f"{self.name} the {self.species} is carrying its baby"

class Aviary(Animal):
    def __init__(self):
        self.birds = []

class ReptileEnclosure(Animal):
    def __init__(self):
        self.reptiles = []