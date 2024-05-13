class Citizen:

    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2

    #direct assignment of variables
    # def sum(self,a,b,c):
    #     s=a+b+c
    #     return s

    #Method overloading:
    def sum(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s


s1=Citizen(21,54)

#print(s1.sum(2,4,5))
print(s1.sum(21,41))
print(s1.sum(21))
print(s1.sum())

