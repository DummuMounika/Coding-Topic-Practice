#if statement
#here indentation is for block of code rather than using flower bracket
temp = 15
if temp > 30:
    print("It's a hot day")
    print("drink plenty of water")
elif(temp > 20):
    print("It's a nice day, enjoy!")
elif(temp > 10):
    print("It's a bit cold")
else:
    print("It's cold")

#exercise
weight = float(input("Please enter your weight"))
unit = input("(K)gs or (L)bs:")
if unit == "K":
    convert = weight/0.45
    print("weight in lbs: ", convert)
else:
    convert = weight*0.45
    print("weight in kgs:", convert)