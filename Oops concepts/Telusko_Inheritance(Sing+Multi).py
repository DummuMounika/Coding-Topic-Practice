#single level inheritance
#sub or child class can access the above parent,grand parent classes
class A:  #super class
    def feature1(self):
        print("Feature 1 working")
    def feature2(self):
        print("Feature 2 working")
class B(A):  #child class or sub class
    #class B is inherit the class A
    #single-level-inheritance
    def feature3(self):
        print("Feature 3 working")
    def feature4(self):
        print("Feature 4 working")

class C(B):  #class have sub and super class
    #class C  inherit the class A &B
    #multi-level-inheritance
    def feature5(self):
        print("Feature 5 working")
a1=A()

#a1.feature1()
#a1.feature2()

b1=B()
# b1.feature1()
# b1.feature2()
# b1.feature3()
# b1.feature4()

c1=C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()