class Person:
    name = "";
    __age = 0;
    __year = 0;

    def __init__(self, name, year): # argumental constructor
        self.name=name #Public variable
        self.__year=year #Private variable

    def getDOB(self): # get the year data
        return self.__year

    def setDOB(self,newdob): # update the year data
        self.__year=newdob

    # encapsulation comes into the picture when ever we call getter and setter to the variable
    def getAge(self):  # get the age data
        return self.__age

    def __setAge(self, newAge):  # set the age data
       self.__age = newAge

    def __calculateAge(self): # Calculate age based on year
        self.__setAge(2024-self.getDOB())
        #self.__age= 2024-self.getDOB()
