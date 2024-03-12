class Organism:
    alive = True

class Animal(Organism):
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

dog = Dog()
print(dog.alive)
dog.eat()