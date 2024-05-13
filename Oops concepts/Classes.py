#creation of class:
class myclass:
    #x=0 #local variable
    #z=0
    #def __init__(self): #default constructor
        #print("hello")
    def __init__(self,xValue,zValue): #Argument constructor
        self.__z=zValue #private
        self.x=xValue

#create a object

y = myclass(12,24)
#print(y.x)

#z = myclass()
#print(z.x)
