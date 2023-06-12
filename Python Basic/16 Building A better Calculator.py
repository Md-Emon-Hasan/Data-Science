# building a calculator
num1 = float(input("Enter first number: "))
op = input("Enter any operator: ")
num2 = float(input("Enter Second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid input")
