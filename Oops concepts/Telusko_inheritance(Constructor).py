#Constructors
#Super class cannot access any features of sub class
#Method Resolution Order
class A:  #super class
    def __init__(self):
        print("in A Init")
    def feature1(self):
        print("Feature 1 working")
    def feature2(self):
        print("Feature 2 working")
# class B(A):  #child class or sub class
class B:
    def __init__(self):
        #if u wanna call the super init method
        #add super method
        #super().__init__()
        print("in B Init")
    def feature3(self):
        print("Feature 3 working")
    def feature4(self):
        print("Feature 4 working")


class C(A,B):
    def __init__(self):
        super().__init__()
        print("in C Init")

    def feat(self):
        super().feature4()

#a1=A()
#a1.feat()
# a1=B()
#if u create obj of subclass it will try to find init of sub class
#if it is not it will call the init in super class
a1=C()
#a1.feature3()
a1.feat()
#prefer to left one first
