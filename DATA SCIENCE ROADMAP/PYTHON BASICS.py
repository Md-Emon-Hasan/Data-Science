# Introduction
print('introduction:')
print('Goodbye world')

# Syntax,Comments,Variables,Data types
print('Syntax,Comments,Variables,Data types:')
# syntax
print('this is syntax')

# comments
# this is commnets

# variable
x = 10
print(x)

# data types
print('data types:')
x = int(10)
print(x)

x = 10
print(x)

x = 'hello emon'
print(x)

# Number, Casting
print('Number, Casting:')
x = 10
y = x
print(x)
print(y)

# string
print('string:')
# print new line
print('hello\nworld')

# store a variable
phrase = 'hello world'
print(phrase)

phrase = 'hello '
print(phrase + 'world')

# convert into lowercase
phrase = 'Hello worLD'
print(phrase.lower())

# convert into uppercse
phrase = 'hello world'
print(phrase.upper())

# check the is uppercase or not
phrase =  'hello world'
print(phrase.isupper())
print(phrase.islower())

# check the is lowercase or not
phrase = 'HELLO WORLD'
print(phrase.isupper())
print(phrase.islower())

phrase = 'hello world'
print(phrase.upper().isupper())
print(phrase.upper().islower())
print(phrase.lower().isupper())
print(phrase.lower().islower())

# check the leangth of the string
phrase = 'good bye world'
print(len(phrase))

# print a character into string
phrase = 'good bye world'
print(phrase[5])

# find index number into string
phrase = 'hello world'
print(phrase.index('w'))

# replace one string to another
phrase = 'hello world'
print(phrase.replace('world', 'Dhaka'))

# operator
x = 10
print(x)

x = 3
x + 3
print(x)

x = 3
x - 3
print(x)

x = 3
x = x * x
print(x)

x = 3
x = 10 / x
print(x)

x = 3
x = 10 % x
print(x)

x = 3
x ** x
print(x)

x = 5
x >>= 3
print(x)

x = 5
x <<= 3
print(x)

# list
print('list:')

mylist = list()
print(mylist)
mylist = []
print(mylist)

friends = ['kevin', 'karan', 'jim']
print(friends)

friends = ['kevin', 'karan', 'jim']
print(friends[0])

friends = ['kevin', 'karan', 'jim', 'oscar', 'toby']
print(friends[-1])

friends = ['kevin', 'karan', 'jim', 'oscar', 'toby']
print(friends[1:3])

friends = ['kevin', 'karan', 'jim', 'oscar', 'toby']
friends[1] = 'hello'
print(friends)

# allow anything list
mylist = [5, True, 'appale']
print(mylist)

# allow duplicate element
mylist = ['apple', 'apple']
print(mylist)

# with using for loop
mylist = ['banana','cherry','apple']
for i in mylist:
    print(i)

# append list
mylist = ['banana','cherry','apple']
mylist.append('lemon')
print(mylist)

# insert function
mylist = ['banana','cherry','apple']
mylist.insert(1,'bluebarry')
print(mylist)

# use pop for remove last element
mylist = ['banana','cherry','apple']
mylist.pop(1)
print(mylist)

mylist = ['banana','cherry','apple']
mylist.pop()
print(mylist)

# remove function
mylist = ['banana', 'cherry', 'apple']
mylist.remove('cherry')
print(mylist)

# reverse function
mylist = ['banana','cherry','apple']
mylist.reverse()
print(mylist)

# sort function
mylist = ['banana','cherry','apple']
mylist.sort()
print(mylist)

mylist = [5,9,3,4,-6,-9,-2]
mylist.sort()
print(mylist)

mylist = [5,9,3,4,-6,-9,-2]
newlist = sorted(mylist)
print(newlist)

# multiple list
mylist = [1,2,3,4] * 5
print(mylist)

# adding list
mylist1 = [1,2,3,4,5]
mylist2 = [6,7,8,9,10]
mylist = mylist1 + mylist2
print(mylist)

# slicing index
mylist = [1,2,3,4,5,6,7,8,9]
a = mylist[1:5]
print(a)

mylist = [1,2,3,4,5,6,7,8,9]
a = mylist[:5]
print(a)

mylist = [1,2,3,4,5,6,7,8,9]
a = mylist[1:]
print(a)

mylist = [1,2,3,4,5,6,7,8,9]
a = mylist[::1]
print(a)

# jumping one by one
mylist = [1,2,3,4,5,6,7,8,9]
a = mylist[::2]
print(a)

# reverse list
mylist = [1,2,3,4,5,6,7,8,9]
a = mylist[::-1]
print(a)

# list copy
list_original = ['banana','cherry','apple']
list_copy = list_original
print(list_copy)

list_original = ['banana','cherry','apple']
list_copy = list_original.copy()
list_copy.append('lemon')
print(list_copy)
print(list_original)

mylist = [1,2,3,4,5,6,7,8,9]
b = [i*i for i in mylist]
print(mylist)
print(b)

# tuples: ordered, immuatable, allows duplicate element
print('tuples: ordered, immuatable, allows duplicate element:')
mytuple = ('max',28,'boston')
print(mytuple)

mytuple = ('max')
print(type(mytuple))

mytuple = tuple(['max',28,'boston'])
print(mytuple)

mytuple = tuple(['max',28,'boston'])
item = mytuple[2]
print(item)

mytuple = ('max', 28, 'boston')
print(mytuple)
for i in mytuple:
    print(i)
    
# length function
mytuple = ('a','p','p','l','e')
print(mytuple.count('p'))
print(mytuple.count('l'))
print(mytuple.count('0'))

# find index value
mytuple = ('a','p','p','l','e')
print(mytuple.index('e'))

mytuple = ('a','p','p','l','e')
mylist = list(mytuple)
print(mylist)
mytuple2 = tuple(mylist)
print(mytuple2)

# sets: unordered, mutable, no duplicates
print('#sets: unordered, mutable, no duplicates:')
myset = {1,2,3,4,5,6}
print(myset)

myset = {1,2,3,1,2,4}
print(myset)

myset = set('hello')
print(myset)

myset = {}
print(myset)

myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
print(myset)

myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
myset.discard(3)
print(myset)

# use pop function
myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
mylist.pop()
print(mylist)

# using for loop
myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
for x in myset:
    print(x)
    
# if statement
myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
if 3 in myset:
    print('yes')

myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
if 4 in myset:
    print('no')
    
# using union function
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
mprims = {2, 3, 5, 7, 11}
unions = odds.union(evens)
print(unions)

# using intersection function
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
mprims = {2, 3, 5, 7, 11}
intersection = odds.intersection(evens)
print(intersection)
intersection = odds.intersection(mprims)
print(intersection)

# using difference function
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
difference = setB.difference(setA)
print(difference)

# using symmetric difference function
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
symmetric_difference = setA.symmetric_difference(setB)
print(symmetric_difference)

# using update function
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
update = setA.update(setB)
print(update)

# using intersection update function
setA = {1, 2, 3, 4, 6, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.intersection_update(setB)
print(setA)

# using difference update function
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.difference_update(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setB.difference_update(setA)
print(setB)

# using symmetric difference update
setA = {1, 2, 3, 4, 6, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.symmetric_difference_update(setB)
print(setA)

# using issubset function
etA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
print(setB.issubset(setA))

# using issuperser function
setA = {1, 2, 3, 4, 5, 6, 7, 8}
setB = {1, 2, 3, 4, 5, 6, 7}
print(setB.issuperset(setA))

# using issuperser function
setA = {1, 2, 3, 4, 5, 6, 7, 8}
setB = {1, 2, 3, 4, 5, 6, 7, 8}
print(setB.issuperset(setA))

# using indisjoint section
setA = {1,2,3,4,5,6}
setB = {1,2,3}
print(setA.isdisjoint(setB))

setA = {1,2,3,4,5,6}
setC = {7,8}
print(setA.isdisjoint(setC))

# creating dictionaries
print('creating dictionaries:')
mydict = {'name':'max','age':28,'city':'new work'}
print(mydict)

mydict = dict(name = 'mary', age = 27, city = 'boston')
value = mydict['age']
print(value)
value = mydict['city']
print(value)

mydict['email'] = 'coolmax@xyz.com'
print(mydict)

# for remove value
mydict = {'name':'max','age':28,'city':'new york'}
print(mydict)
del mydict['name']
print(mydict)

# for remove value
mydict = {'name':'max','age':28,'city':'new york'}
print(mydict)
mydict.pop('age')
print(mydict)

# for remove value
mydict = {'name':'max','age':28,'city':'new york'}
print(mydict)
mydict.popitem()
print(mydict)

# using if statement
mydict = {'name':'max','age':28,'city':'new york'}
if 'name' in mydict:
    print(mydict['name'])
    
# using for loop 
mydict = {'name':'max','age':28,'city':'new york'}
for key in mydict:
    print(key)
    
mydict = {'name':'max','age':28,'city':'new york'}
for key in mydict.values():
    print(key)
    
# using copy
mydict = {'name':'max','age':28,'city':'new york'}
mydict1 = mydict
print(mydict1)

mydict = {'name':'max','age':28,'city':'new york'}
mydict1 = mydict
mydict1['email'] = 'max@xyz.com'
print(mydict1)
print(mydict)

# actual copy
mydict = {'name':'max','age':28,'city':'new york'}
mydict1 = mydict.copy()
mydict1['email'] = 'max@xyz.com'
print(mydict)
print(mydict1)

print('using if statement:')
mydict = {'name':'max','age':28,'city':'new york'}
mydict1 = dict(mydict)
mydict1['email'] = 'max@xyz.com'
print(mydict)
print(mydict1)

# update dictionaries
mydict = {'name':'max','age':28,'email':'max@xyz.com'}
mydict1 = dict(name = 'Marry', age = 27, city = 'boston')
mydict.update(mydict1)
print(mydict)

# integer data types
mydict = {3:9, 6:36, 9:81}
print(mydict)

# print with specific value
mydict = {3:9, 6:36, 9:81}
value = mydict[3]
print(value)

mutuple = (8,7)
mydict = {mytuple: 15}
print(mydict)

MonthConversation = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
}
print(MonthConversation['Apr'])
print(MonthConversation.get('Jan'))
print(MonthConversation.get('Hello','Not a valid input'))

# if else statement
print('if else statement:')
is_male = True
if is_male:
    print('you are male')
    
is_male = True
if is_male:
    print('you are a male')
else:
    print('you are not a male')
    
is_male = True
is_tall = False
if is_male or is_tall:
    print('you are male or tall or both')
else:
    print('you are neither male or tall')
    
is_male = True
is_tall = False
if is_male and is_tall:
    print('you are a male and tall')
elif is_male and not is_tall:
    print('you are a male but not a tall')
elif not is_male and is_tall:
    print('you are not a male but tall')
else:
    print('you are neither male or tall')
    
# if else statement and compariasion
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
result =  max_num(4,5,6)
print(result)

# While loops and for loops
print('while loops and for loops:')
i = 1
while i <= 5:
    print(i)
    i += 1

for letter in 'bangladesh':
    print(letter)
 
friends = ['jim', 'karan', 'kevin']
for friend in friends:
    print(friend)

# for loop with range function
for index in range(10):
    print(index)
print('end the loop')    

for index in range(3, 10):
    print(index)
print('end of the loop')

friends = ['jim','karan','kevin']
for index in range(len(friends)):
    print(index)
print('end of loop')    

for index in range(5):
    if index == 0:
        print('first interation')
    else:
        print('not first')

# functions
print('functions:')
def say_hi():
    print('hello users')
print('top')
say_hi()
print('bottoom')

def say_hi():
    print('hello users')
say_hi()
say_hi()

# function with perameter
def say_hi(name):
    print('hello',name)
say_hi('emon')
say_hi('hasan')

def say_hi(name, age):
    print("Hello " + name + "! You are " + age + "." )
say_hi('emon','20')
say_hi('hasan','20')

def foo(a,b,c):
    print(a,b,c)
foo(1,2,3)

# functon with different valule
def foo(a,b,c):
    print(a,b,c)
foo(1, b=2, c=3)

# function with different value
def foo(a,b,c,d=4):
    print(a,b,c,d)
foo(1,2,3)

def foo(a,b,c,d=4):
    print(a,b,c,d)
foo(1,2,3,7)

# function with args value
def foo(a,b,*args, **kwargs):
    print(a,b)
    for arg in args:
        print(arg)
foo(1,2,3,5,6,7)

# function woth args and kwargs
def foo(a,b,*args,**kwargs):
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])
foo(1,2,3,4,six=6,seven=7)

def foo(a,b,*args,**kwargs):
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key,kwargs[key])
foo(1,2,3,4,5)

def foo(a,b,*,c,d):
    print(a,b,c,d)
foo(1,2,c=3,d=4)

def foo(*args, last):
    for arg in args:
        print(arg)
    print(last)
foo(1,2,3,last=300)

def foo(a,b,c):
    print(a,b,c)
my_list=(0,1,2)
foo(*my_list)

def foo(a,b,c):
    print(a,b,c)
mydict ={'a':1,'b':2,'c':3}
foo(**mydict)

# function with global number
def foo(a_list):
    a_list.append(4)
mylist = [1,2,3]
foo(mylist)
print(mylist)

def foo(a_list):
    a_list.append(4)
    a_list[0] = -100
my_list = [1,2,3]
foo(my_list)
print(my_list)

def foo(a_list):
    a_list += [200, 300, 400]
my_list = [1,2,3]
foo(my_list)
print(my_list)

def foo(a_list):
    a_list = a_list + [200,300,400]
foo(my_list)
print(my_list)

# user input
# print('uset input:')
# name = input('enter your name: ')
# print('are you: ' + name)

# name = input('enter your name: ')
# age = input('enter your age: ')
# print('hello ' + name + '! you are ' + age + '.')

# try except
try:
    value = 10/0
    number = int(input('enter any number: '))
    print('your number is: ' + number)
except ZeroDivisionError:
    print('divided by number')
except ValueError:
    print('invalid input')
    
try:
    value = 10/0
    number = int(input('enter number is:'))
    print('your number is: ' + number)
except ZeroDivisionError as emon:
    print(emon)
except ValueError:
    print('invalid input')
    
# error and ecxeption
# x = -5
# if x < 0:
#     raise Exception('x should be positive')

x = 5
if x < 5:
    raise Exception('x should be posetive')

# ussing assertion error
# x = - 5
# assert(x>=0), 'x is not posetive'

# zero division error
# a = 5 / 0

try:
    a = 5 / 0
except:
    print('an error detected')
    
# using try except with error message
try:
    a = 5 / 0
except Exception as e:
    print(e)
    
# using multiple exception
try:
    a = 5 / 1
    b = a + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
    
# using with else
try:
    a = 5 / 1
    b = a + 10
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine')
    
# using try with except with else and finally
try:
    a = 5 / 0
    b = a + 10
except TypeError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print('everything is fine')
finally:
    print('cleaning up...')
    
try:
    a = 5 / 1
    b = a + 10
except TypeError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print('everything is fine')
finally:
    print('cleaning up...')
    
# check value check
# class ValueTooHighError(Exception):
#     pass
# def test_value(x):
#     if x > 100:
#         raise ValueTooHighError('value is too high')
# test_value(101)

class ValueTooHighError(Exception):
    pass
def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
try:
    test_value(200)
except ValueTooHighError as e:
    print(e)
    
class ValueTooHighError(Exception):
    pass
class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.messege = message
        self.value = value
def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is to high')
    if x < 100:
        raise ValueTooSmallError('value is too small',x)
    try:
        test_value(20)
    except ValueTooHighError as e:
        print(e)
    except ValueTooSmallError as e:
        print(e.messege, e.value)

# lambda function
add10 = lambda x: x + 10
print(add10(5))

mul = lambda x,y: x + y
print(mul(2,3))

mul = lambda x,y: x * y
print(mul(5,7))

# using sorted function
print('using shot function:')
point2D = [(1,2), (15,1), (5,-1), (10,4)]
point2D_sorted = sorted(point2D)
print(point2D)
print(point2D_sorted)

# sorted with y index
point2D = [(1,2),(15,1),(5,-1),(10,4)]
point2D_sorted = sorted(point2D, key=lambda x: x[1])
print(point2D)
print(point2D_sorted)

point2D = [(1,2),(15,1),(5,-1),(10,4)]
point2D_sorted = sorted(point2D, key=lambda x: x[0] + x[1])
print(point2D)
print(point2D_sorted)

# using map(func, seq) function
print("using map(func, sequence):")
a = [1,2,3,4]
b = map(lambda x: x * 2, a)
print(list(a))
print(list(b))

a = [1,2,3,4]
c = [x * 2 for x in a]
print(a)
print(list(c))

# using filter function
print('using filter function:')
a = [1,2,3,4]
b = map(lambda x: x % 2 == 0, a)
print(list(b))

a = [1,2,3,4]
b = filter(lambda x: x % 2 == 0, a)
print(list(b))

# second method
a = [1,2,3,4]
c = [x for x in a if x % 2 == 0]
print(list(c))

# using reduce(func, seq) function
print('usinig reduce(func, seq) function:')
from functools import reduce
a = [1,2,3,4]
b = reduce(lambda x,y: x * y, a)
print(b)

a = [1,2,3,4]
b = reduce(lambda x,y: x + y, a)
print(b)