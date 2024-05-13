class Computer: #created a class

    def __init__(self,cpu,ram):
        #called automatically for every object
        print("Hello")
        self.cpu = cpu
        self.ram = ram

    def config(self):
        #default constructor
        print("config is", self.cpu, self.ram)

com1 = Computer('i5',16)
#instance1 or object1
com2 = Computer('Mounika 5',8)
#instance2 or object2
#Computer.config(com1) #calling com1 as a parameter
#Computer.config(com2)  #calling com2 as a parameter
com1.config()
#config will take com1 as a parameter
com2.config()
#config will take com2 as a parameter
