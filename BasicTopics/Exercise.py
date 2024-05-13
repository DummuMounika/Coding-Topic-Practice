firstNumber = float(input("enter your first number: "))
operator = input("enter (+  or - or * or / or %) :")
secondNumber = float(input("enter your second number: "))
if operator == "+":
    print(firstNumber+secondNumber)
elif operator == "-":
    print(firstNumber-secondNumber)
elif operator == "*":
    print(firstNumber*secondNumber)
elif operator == "/":
    print(firstNumber/secondNumber)
elif operator == "%":
    print(firstNumber%secondNumber)
else:
    print("invalid operation")