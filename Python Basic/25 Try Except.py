# try except
try:
    value = 10/0
    number = int(input("Enter any number: "))
    print("Your number is: " + number)
except ZeroDivisionError:
    print("Divided by number")
except ValueError:
    print("Invalid input")

try:
    value = 10 / 0
    number = int(input("Enter any number: "))
    print("Your number is: " + number)
except ZeroDivisionError as emon:
    print(emon)
except ValueError:
    print("Invalid input")

