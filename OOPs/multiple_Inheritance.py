#multiple inheritance : where a child class is derived from more than one parent class

class prey:
    def flee(self):
        print("This animal is flees")

class predator:
    def hunt(self):
        print("This animal is hunting")


class Rabbit(prey):
    pass

class Hawk(predator):
    pass

class Fish(prey,predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()
