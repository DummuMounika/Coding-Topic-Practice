class Computer:
    #pass
    def __init__(self):
        self.name = "Monu"
        self.age = 23

    def update(self):
        self.age = 24

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False

c1 = Computer() #internally the init constructor  is calling
c1.age = 26
c2 = Computer()
#memory allocation
# print(id(c1))
# print(id(c2))
c1.name = "Venu"
# c1.age = 26
#updating the values for the parameter
print(c1.name)
print(c2.name)
#c1.update()
#print(c1.age)

if c1.compare(c2): #compare(who is calling,whom to compare)
    print("Same")
else:
    print("Different")
