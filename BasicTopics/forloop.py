#for loop for iterating each value in the list and gives in separate line
numbers = [1,2,3,4,5]
for items in numbers:
    print(items)

#range function to generate sequence of number
numbers = range(5) # will have value from 0 to 5
for number in numbers:
    print(number) #0 to 4
numbers = range(5,10) # will have value from 0 to 5
for number in numbers:
    print(number) #5 to 9
numbers = range(5,20, 2) # jump +2
for number in numbers:
    print(number) #0 to 4

#tuples are the sequence of object but it's unchangable
numbers = (1,2,3)
#it is declared only when user don't want to change the list of objects in tuple