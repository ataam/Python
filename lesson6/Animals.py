class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
    def makeSound(self, sound):
        self.sound = sound
        print(self.sound)

animalP = Animal("Puppy","monkey",13)
print(animalP.__dict__)
animalP.makeSound("Uuaa")
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
animalA = Animal("Annuzi","Dog",11)
print(animalA.__dict__)
animalA.makeSound("Bark")







