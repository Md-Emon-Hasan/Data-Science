# conditions
print("condition:")
x = 2
print(x == 2)
print(x == 3)
print(x < 3)

# Boolean operators
print("Boolean operators:")
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old")
if name == "John" or name == "Rick":
    print("Your name is either John or Risk")

# in operator
print("in operator:")
name = "John"
if name in ["John", "Risk"]:
    print("Your name is either John or Risk")

# is, else if and else
print("if, elseif and else:")
statement = False
another_statement = True
if statement is True:
    ''' do something '''
    pass
elif another_statement is True:
    ''' do something else '''
    pass
else:
    ''' do another thing '''
    pass

# is and else
print("if and else:")
x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two")

# using is operator
print("using is operator:")
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)

# using not operator
print("using not operator:")
print(not False)
print((not False) == (False))

# erercise
print("exercise:")
number = 20
second_number = 0
first_array = [1, 2, 3]
second_array = [1, 2]

if number > 15:
    print("1")
if first_array:
    print("2")
if len(second_array) == 2:
    print("3")
if len(first_array) + len(second_array) == 5:
    print("4")
if first_array and first_array[0] == 1:
    print("5")
if not second_number:
    print("6")
