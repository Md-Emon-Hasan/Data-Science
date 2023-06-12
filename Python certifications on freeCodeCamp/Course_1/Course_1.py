# assignment variable
print("assignment variable:")
x = 2
print(x)

x = 2
print(x)
x = x + 2
print(x)

# conditional statement
print("conditional statement:")
x = 5
if x < 10:
    print("Smaller")
if x > 20:
    print("Bigger")
print("Finished")

# loop
print("loop:")
n = 5
while n > 0:
    print(n)
    n = n - 1
print("Blastoff")

# constant
print("constant:")
print(123)
print(98.6)
print("hello world")

# variable
print("variable:")
a = 35.0
b = 12.50
c = a * b
print(c)

x = 3.9 * x * (1 - x)
print(x)

# numeric expression
print("numeric expression:")
xx = 2
xx = xx + 2
print(xx)

yy = 440 * 12
print(yy)

zz = yy / 1000
print(zz)

jj = 23
kk = jj % 5
print(kk)

print(4 ** 3)

ddd = 1 + 4
print(ddd)

eee = "hello " + "there"
print(eee)

# check type
print("check type")
eee = "hello"
print(type(eee))

eee = 1
print(type(eee))

temp = 98.6
print(type(temp))

# type conversions
print("type conversions")
print(float(99) + 100)
i = 42
print(type(i))
f = float(i)
print(f)
print(type(f))

# integer devision
print("integer conversions:")
print(10 / 2)
print(9 / 2)
print(99 / 100)
print(10.0 / 2.0)
print(99.0 / 100.0)

# string conversion
print("string conversions:")
sval = "123"
ival = int(sval)
print(ival + 1)

# user input
print("user input:")
nam = input("who are you?")
print("welcome", nam)

# conditional steps
print("conditional steps:")
x = 5
if x < 10:
    print("smaller")
if x > 20:
    print("Bigger")
print("Finis")

x = 5
if x == 5:
    print("Equals 5")
if x > 4:
    print("Greater then 4")
if x >= 5:
    print("Greater then or equals 5")
if x < 6:
    print("Less then 6")
if x <= 5:
    print("Less than or equal 5")
if x != 6:
    print("Not equal 6")

# nested dicision
print("nested dicision:")
x = 42
if x > 1:
    print("More than one")
    if x < 100:
        print("Less than 100")
print("All done")

# two way decision with else
print("two way decision with else:")
x = 4
if x > 2:
    print("Bigger")
else:
    print("Smaller")
print("All done")

# multil-way
print("multi-way:")
x = 2
if x < 2:
    print("Small")
elif x < 10:
    print("Medium")
else:
    print("Large")
print("All done")

# tet-except
astr = "Hello Bob"
try:
    istr = int(astr)
except:
    istr = -1
print("First", istr)

astr = "123"
try:
    istr = int(astr)
except:
    istr = -1
print("second", istr)

astr = "Bob"
try:
    print("Hello")
    istr = int(astr)
    print("there")
except:
    istr = -1
print("Done", istr)

# stored steps
print("stored steps:")
def thing():
    print("Hello")
    print("Fun")
thing()
print("zip")
thing()

# max fuction
print("max function:")
big = max("Hello world")
print(big)
tiny = min("Hello world")
print(tiny)

# function
print("function:")
def hello():
    print("hello emon")
hello()

# function with perameter
print("function with perameter:")
def greet(lang):
    if lang == "es":
        print("Hola")
    elif lang == "fr":
        print("Bonjour")
    else:
        print("hello")
greet("es")
greet("fr")
greet("en")

def greet(lang, country):
    print("language = " + lang)
    print("country = " + country)
greet("english", "england")

# function with return values
print("function with return values:")
def greet():
    return "Hello"
print(greet(), "Gleen")
print(greet(), "sally")

def greet(lang):
    if lang == 'es':
        return "Hola"
    elif lang == "fr":
        return 'Bonjour'
    else:
        return 'hello'
print(greet('en'), 'Glenn')
print(greet('es'), 'Sally')
print(greet('fr'), 'Michael')

# loops and iteration
print("loops and iteration:")
n = 5
while n > 0:
    print(n)
    n = n - 1
print("Blastoff")
print(n)

n = 5
while n > 0:
    print("Lather")
    print("Rinse")
    n = n - 1
print("Dry off!")

# breaking out of a loop
'''
print("breaking out of a loop:")
while True:
    line = input("> ")
    if line == "done":
        break
    print(line)
print("Done!")
'''

'''
print("breaking out of a loop:")
while True:
    line = input("> ")
    if line == "#":
        continue
    if line == "done":
        break
    print(line)
print("Done!")
'''

# definite loop
print("definite loop:")
for i in [5, 4, 3, 2, 1]:
    print(i)
print("Blastoff!")

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print("happy new year:", friend)
print("Done!")

# looping through a set
print("looping through a set:")
print('before')
for thing in [9, 42, 12, 3, 74, 15]:
    print(thing)
    
zork = 0
print('Beofre', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print("after", zork)

# summing in a loop
print('summing in a loop:')
zork = 0
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + thing
    print(zork, thing)
print('after', zork)

# finding the average in a loop
print('finding the average in a loop:')
count = 0
sum = 0
print('before', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('after', count, sum, sum / count)

# filtering in loop
print('filtering in loop:')
print("before")
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print('large number:', value)
print('after')

# search using a boolean variable
print('search using a boolean variable:')
found = False
print("Before", found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found == True
    print(found, value)
print('after', found)

# find the larger value
print('find the larger value:')
smallest_so_far = -1
print("Before", smallest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num < smallest_so_far:
        smallest_so_far = the_num
    print(smallest_so_far, the_num)
print('after', smallest_so_far)

# finding the smallest value
print('finding the smallest value:')
smallest = None
print("Before")
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('after', smallest)