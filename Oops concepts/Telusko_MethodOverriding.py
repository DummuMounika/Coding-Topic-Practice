class A:
    def show(self):
        print("in A show")

#Method Overriding
class B(A):
    def show(self):
        print("in B show")


#a1=A()
a1=B()
a1.show()