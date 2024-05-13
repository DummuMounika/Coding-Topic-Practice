class Employee:

    def __init__(self, first, last, pay):
        self.first= first
        self.last=last
        self.pay=pay
        self.email= first + '' + last + '@company.com'
    #method
    #self must be arugment to use the variables
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
#instance created
emp_1 = Employee('Mounika','Dummu',5436972)
emp_2 = Employee('Venu','Dummu',7836972)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())

print(Employee.fullname(emp_1))