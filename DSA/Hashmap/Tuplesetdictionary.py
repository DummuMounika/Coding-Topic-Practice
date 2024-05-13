#tuple define with ()
students = ("monu", "venu","venu",9,9 ,"akhi", "rns", "deepu")
#students[0] = "Monu" #throws error as tuple' object does not support item assignment
print(students.index("venu"))
print(students.count(9))
print(students)
#set define with {} and it stores unique value
#in set index doesn't exit and it is called unordered
marks = {98,99,99,76,89}
for score in marks:
    print(score)
#dictornary have key and value and it is also unordered
marks= {"english": 98, "hindi": 99, "chemistry": 98}
print(marks["chemistry"]) #to get only chemistry subject
marks["physics"]= 96 # to add new key and value in the dictionary
print(marks)

marks["physics"] = 99 #to change the existing assigned value
print(marks)
