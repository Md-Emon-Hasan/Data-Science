# variables
print("variables:")
myint = 7
print(myint)

# variables with float
print("variables with float:")
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

# variables with string
print("variables with string:")
mystring = "hello"
print(mystring)
mystring = "hello"
print("mystring")

mystring = "Don't worry about apostrophes"
print(mystring)

# variables with simultaneously
print("variables with simultaneously:")
a, b = 3, 4
print(a, b)

# erercise
print("exercise:")
mystring = "hello"
myfloat = 10.0
myint = 20

if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
