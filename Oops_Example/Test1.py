from Student import Student

class Test1:
    student1 = Student(121,"Monu",2000)
    print("Age after constructor:::", student1.getAge())



    print("Id::",student1.getId())
    print("Name::",student1.getName())
    print("Age::",student1.getAge())
    print("year:", student1.getYear())


    print("Before Id::", student1.getId())
    student1.setId(9348)
    print("After Updating Id::",student1.getId())

    print("Before Name::", student1.getName())
    student1.setName("Venu")
    print("After Updating name:",student1.getName())

    print("Before Update-Age::", student1.getAge())
    student1.setYear(1998)
    print("Update-Year::",student1.getYear())
    print("After Updated-Age::",student1.getAge())

    #student2 = Student()
    #print(student2.id)
    #print(student2.name)
    #print(student2.age)