from Person import Person

class Test:
    p1 = Person('Mounika', 2000)
    print(p1.name)

    print("Bef",p1.getDOB())
    p1.setDOB(1998)
    print("Aft", p1.getDOB())
    print("Bef Age", p1.getAge())
    print("After Age",p1.getAge())
