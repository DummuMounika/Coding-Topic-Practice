#Tuple is a collection which is ordered and unchangeable or immutable .Allows duplicate
#Tuples are written with round brackets.
languages=("Hindi","Telugu","German","English","French","English",1)
print(languages[0]) #ordered and we can access the single element in the list
''''
Below code will throw error as "TypeError: 'tuple' object does not support item assignment
languages[2] = "Marathi" 
print(languages)
print(languages.append("Kannada")) #tuple cannot even add elements
print(languages.insert(0,"Oriya")) #tuple cannot even insert element
'''
print(languages) #allows duplicate elements in the list
print(len(languages)) #return the length of tuple list element count

#Tuple have 2 methods that are index and count
print(languages.count("French")) #it returns the count of the element
print(languages.index(1)) #it returns the index value
#for loop
for i in range(len(languages)):
    print(languages[i])

print(">>>>>>>>>>>>>>>>>>>>")

for language in languages:
    print(language)

