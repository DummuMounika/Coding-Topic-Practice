#Set is collection which is unordered,unchangeable or immutable.Doesn't allow duplicate only have unique elements in the list
#Sets are written with curly brackets.
food = {"Dosa", "Poha", "Idli","Upma","Poori","Dosa","Poha"}
print(food) #only stores unique elements in the list
'''
 #'set' object does not support item assignment
# food[0]= "Masala Dosa"  #unchangable
print(food) 
'''
'''
'set' object is not subscriptable
for i in food: 
    print(food[i])  #unordered
    i+=1
'''
food.add("sambar")
food.remove("Poha")
foods= food.copy()
#food.clear()
foods.add("vada")
unionfoods= food.union(foods)
print(foods)
for i in unionfoods:
    print(i)

