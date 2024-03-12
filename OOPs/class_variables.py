#class variable vs instance variables
class Car:
    wheels = 4 # class varible

    #constructor
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

print(Car.wheels)
