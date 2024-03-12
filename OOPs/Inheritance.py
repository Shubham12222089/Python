class Animal:

    alive = True

    def eat(self):
        print("Animal is eating")

    def sleep(self):
        print("Animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("Rabbit is running")
class Fish(Animal):
    def swim(self):
        print("Fish is swimming")
class Hawk(Animal):
    def fly(self):
        print("Hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

# print(rabbit.alive)
# fish.eat()
# hawk.sleep()
hawk.fly()
fish.swim()