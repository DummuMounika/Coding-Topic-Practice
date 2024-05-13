class Student: #Outer Class

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name ,self.rollno)
        self.lap.show()

    #Inner Class
    class Laptop:

        def __init__(self):
            self.brand ='HP'
            self.cpu = 'i7'
            self.ram = 8

        def show(self):
            print(self.brand,self.cpu,self.ram)

s1 = Student('Monu',3)
s2 = Student('Venu',4)

s1.show()