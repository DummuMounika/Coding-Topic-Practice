#List is a collection which is ordered and changeable.Allows duplicate element.
#Lists are written with square brackets.
states= ["Delhi","Hyderabad","Viskhapatnam","Punjab","Punjab",1,1,2,3,1]
states.append("Kerala") #for adding new element in the list
print(states)
states.remove("Delhi") #for removing x element in the list
print(states)
print(states[1]) #for printing 1st index element in the list
states[1] = "Vizag" #for replacing the value on that index
print(states)
states.insert(3,"Haryana") #for inserting the value in the index
print(states)
for i in range(len(states)):
    print(states[i])
    i+=1