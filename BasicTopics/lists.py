'''
#lists are used for representing list of objects, names and number
names = ['Monu','Venu','Vijaya','Sekhar']
print(names[0]) #to print first element in the list
print(names[-1]) #to print last element in the list
print(names)
names[0]= "Mounika"#if you want to replace one element in the list
print(names)
#to return only some indexs in the list
print(names[1:3]) #it will return index 1 and 2 value, 3 will not include
print(names)
'''
'''
#List are also objects
#list method
numbers= [1,2,3,4,5]
numbers.append(6) # to add any object in the list
print(numbers)
print(len(numbers)) #for length of numbers in the list
print(6 in numbers)#returns boolean value and to search and confirm the value presence
numbers.insert(0,-1) #to insert any object in the list
print(numbers)
numbers.remove(3) #to remove any object in the list
print(numbers)
numbers.clear() #to clear the list of objects
print(numbers)
'''


