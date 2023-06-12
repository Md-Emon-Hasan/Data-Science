# Functions And Docstrings
a = 9
b = 8
c = sum((a, b))
print(c)

def function1():
    print('hello you are in function 1')
function1()

def function1(a, b):
    print('hello you are in function 1', a + b)
function1(5, 7)

def function1(a, b):
    average = (a + b) / 2
    print(average)
function1(5, 7)

def function1(a, b):
    average = (a + b) / 2
    print(average)
    return average
v = function1(5, 7)
print(v)

def function1(a, b):
    average = (a + b) / 2
    return average
print(function1.__doc__)

print('enter num 1')
num1 = input()
print('enter number 2')
num2 = input()
try:
    print('the sum of these two number is', int(num1) + int(num2))
except Exception as e:
    print(e)
    