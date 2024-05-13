
class Car:

    wheels = 4 #class variables
    def __init__(self):
        self.milage = 10 #instance variables(namespace)
        self.comp = "Audi"

c1 = Car()
c2 = Car()

c1.milage = 8
Car.wheels = 5

print(c1.comp, c1.milage , c1.wheels)
print(c2.comp, c2.milage , c2.wheels)