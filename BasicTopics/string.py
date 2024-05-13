course = 'python for beginners'
print(course.upper()) #it will print new string and convert into uppercase
print(course.lower()) #it will print new string and convert into lowercase
print(course)
print(course.find('y')) #the find method return the index and it's case sensitive
print(course.find('Y')) #it returns -1 when the element is not present
print(course.find('beginners')) #it returns the starting of the word index
print(course.replace('y','4')) #replacing y character with 4
print(course.replace('x','4')) #if teh replacing character is not present it doesn't return anything
#in keyword
print('python' in course) #if it's present it return boolean value as true



