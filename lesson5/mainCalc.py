import Calc

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
operation = input("Enter operation: ")

if operation == "+":
    print(Calc.add(num1,num2))
elif operation == "-":
    print(Calc.sub(num1,num2))
elif operation == "*":
    print(Calc.mul(num1,num2))
elif operation == "/":
    print(Calc.div(num1,num2))
elif operation == "**":
    print(Calc.pow(num1,num2))
else:
    print("Invalid operation")



