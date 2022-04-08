class Animals:
    animalType = "Mammal"

class Pets(Animals):
    color = "White"

class Dog(Pets):
    @staticmethod
    def barks():
        print("Bhaw bhaw")

dog = Dog()

dog.barks()