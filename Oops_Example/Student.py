class Student:
    __age =None
    __name = None
    __id = None
    __year = None

    def __init__(self):# default constructor
        print("This is default constructor")


    def __init__(self,newId,newName,newYear):# Arguments constructor
        self.__id = newId
        self.__name = newName
        self.__year = newYear
        self.__calculateAge()
        print("In constructor:::",self.__age)


    def getYear(self):
        return self.__year

    def setYear(self,updateYear):
        self.__year = updateYear
        self.__calculateAge()


    def __calculateAge(self):
        self.__setAge(2024-self.getYear())

    def getAge(self):# This function returns age data
        return self.__age

    def __setAge(self,newAge): # This function assign the age data
        self.__age=newAge

    def getName(self):# This function returns name data
        return self.__name

    def setName(self,newName):
        self.__name=newName

    def getId(self):# This function returns id data
        return self.__id

    def setId(self,newId):
        self.__id = newId









