class Student:
    #static variable: #class variable
    school ="SAU"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self): #instance method
        return (self.m1 +self.m2 + self.m3)/3

    def get_m1(self):
        return self.m1

    def set_me(self,val): #self is the instance
        self.m1 = val

    @classmethod
    def getschool(cls):  #cls is the instance
        return cls.school

    @staticmethod
    def info():
        print("This is OOPS class")

s1 = Student(23,45,67)
s2 = Student(54,90,98)


print(s1.avg())
print(s2.avg())
print(Student.getschool())
print(Student.info())


