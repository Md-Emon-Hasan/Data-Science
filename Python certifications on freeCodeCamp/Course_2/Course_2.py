# sring in python
# sting data type
print('string data type:')
str1 = "hello"
str2 = "there"
bob = str1 + str2
print(bob)
str3 = '123'
x = int(str3) + 1
print(x)

# reading and converting
print('reading and converting:')
# name = input('enter:')
# print(name)
# apple = input('enter:')
# x = int(apple) - 10
# print(x)

# looking inside strings
print('looking inside string:')
fruit = 'banana'
letter = fruit[1]
print(letter)

fruit = 'banana'
letter = fruit[1]
x = 3
w = fruit[x - 1]
print(w)

# len function
print('len function:')
fruit = 'banana'
x = len(fruit)
print(x)

# looping through strings
print('looping through strings:')
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

fruit = 'banana'
for letter in fruit:
    print(letter)

fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1
    
# looping and counting
print('looping and counting:')
word = "banana"
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

# looking deeper into in
print('looking depper into in:')
for letter in 'banana':
    print(letter)
    
# slicing string
print('slicing string:')
s = 'Monty pyhton'
print(s[0:4])
print(s[6:7])
print(s[6:20])

# string concatenation
print('string concatenation:')
a = 'hello'
b = a + ' there'
print(b)

a = 'hello'
c = a + ' ' + 'there'
print(c)

# using in as a logical operator
fruit = 'banana'
if 'a' in fruit:
    print('Found it!')
    
# strring comparison
print('string comparison:')
word = 'banana'
if word == 'banana':
    print('all right, banana.')
    
word = 'bangladesh'
if word < 'banana':
    print('your word, ' + word + 'comes beofre banana.')
elif word > 'banana':
    print('your word, ' + word + ', comes after banana.')
else:
    print('all right, bananas.')

# string library
print('string library:')
greet = 'Hello Bob'
zap = greet.lower()
print(zap)

print('HI There'.lower())

stuff = "Hello world"
print(type(stuff))
print(dir(stuff))

# searching a string
fruit = "banana"
pos = fruit.find('na')
print(pos)

fruit = "banana"
aa = fruit.find('z')
print(aa)

# making everything upper case
print('making everything upper case:')
greet = 'hello bob'
nnn = greet.upper()
print(nnn)

greet = 'hello bob'
www = greet.lower()
print(www)

# search and replace
print('search and replace:')
greet = 'hello bob'
nstr = greet.replace('bob','jane')
print(nstr)

greet = 'hello bob'
nstr = greet.replace("o", 'x')
print(nstr)

# striping whitespace
print('striping whitespace:')
greet = '     hello bob    '
print(greet.lstrip())

greet = '     hello bob   '
print(greet.rstrip())

greet = '   hello bob   '
print(greet.strip())

# preflixes
print('preflixes:')
line = 'please have a nice day'
print(line.startswith('please'))

line = 'please have a nice day'
print(line.startswith('p'))

data = "from stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
atpos = data.find('@')
print(atpos)

appos = data.find(' ', atpos)
print(appos)

host = data[atpos+1 : appos]
print(host)

# reading file
print("reading file:")
# using open()
print('using open():')
fhand = open('firstfile.txt','r')

# file handle
print('file handle:')
fhand = open('firstfile.txt')
print(fhand)

# the new line character
print('the new line character:')
stuff = 'hello\nworld'
print(stuff)

stuff = 'X\nY'
print(stuff)

# file handle as a sequence
print('file handle as a sequence:')
xfile = open('firstfile.txt')
for cheese in xfile:
    print(cheese)
    
# counting lines in a file
print('counting lines in a file:')
fhand = open('firstfile.txt')
count = 0
for line in fhand:
    count = count + 1
print('line count:', count)

# reading the whole file
print('reading the whole file:')
fhand = open('firstfile.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])

# seaching through a file
print('searching through a file:')
fhand = open('firstfile.txt')
for line in fhand:
    if line.startswith('hello'):
        print(line)

# skipping with continue
print('skipping with continue:')
fhand = open('firstfile.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('hello'):
        continue
    print(line)
    
# searching for a file (fixed)
print('searching for a file:')
fhand = open('firstfile.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('hello'):
        print(line)
        
# prompt with file name
print('prompt for file name:')
# fname = input("enter the file name: ")
# fhand = open(fname)
# count = 0
# for line in fhand:
#     if line.startswith('hello'):
#         count = count + 1
# print('there were', count, 'hello lines in', fname)

# bad file names
print('bad file name:')
# fname = input('enter the file name: ')
# try:
#     fhand = open(fname)
# except:
#     print('file canoot be apened:', fname)
#     quit()
# count = 0
# for line in fhand:
#     if line.startswith('subject:'):
#         count = count + 1
# print('there were', count, 'subject lines in', fname)

# python list
print('python list:')
# what is not a collector
print('what is not a collector:')
x = 2
x = 4
print(x)

# list contants
print('list contants:')
print([1, 24, 76])
print(['red', 'yellow', 'blue'])
print(['red', 24, 96.6])
print([1, [5, 6], 7])
print([])

# lists and definite loops best pals
print('lists and definite loops best pals:')
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy new year', friend)
print('done')

z = ['Joseph', 'Glenn', 'Sally']
for x in z:
    print('Happy new year', x)
print('done')

# looking inside lists
friends = ['Joseph', 'Glenn', 'Sally']
print(friends[1])

lotto = [2, 14, 26, 41, 63]
print(lotto)
lotto[2] = 28
print(lotto)

# how long is a list
print('how long is a list:')
greet =  'hello bob'
print(len(greet))

x = [1, 2, 'joe', 99]
print(len(x))

# using the range function
print('using range function:')
print(range(4))
friends = ['Joseph', 'Glenn', 'Sally']
print(len(friends))
print(range(len(friends)))

# a tele of two loops
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print("Happy new year", friend)

friends = ['Joseph', 'Glenn', 'Sally']
for i in range(len(friends)):
    friend = friends[i]
    print('happy new year', friend)
    
# working with string
# concatenating listls using +
print('concatenating lists using +')
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(a)
print(b)
print(c)

# list can be sliced using
print('list can be sliced using:')
t = [9, 41, 12, 3, 74, 15]
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])

# list methods
print('list methods:')
x = list()
print(type(x))
print(dir(x))

# building a list from scratch
print('builing a list from scretch:')
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)

# is something in a list
print('is something in a list:')
some = [1, 9, 21, 10, 16]
print(9 in some)
print(15 in some)
print(20 not in some)

# lists are in order
print('list are in order:')
friend = ['Joseph', 'Glenn', 'Sally']
friend.sort()
print(friend)
print(friend[1])

# built in function and list
print('built in function and list:')
nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

# total = 0
# count = 0
# while True:
#     inp = input('enter a number: ')
#     if inp == 'done': break
#     value = float(inp)
#     total = total + value
#     count = count + 1
# average = total / count
# print('Avarage:', average)

# string and list
print('string and list:')
abc = 'which theree words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])

stuff = ['with', 'three', 'words']
for w in stuff:
    print(w)
    
line = 'A lot of spaces'
etc = line.split()
print(etc)

line = 'first;second;third'
thing = line.split()
print(thing)
print(len(thing))

line = 'first;second;third'
thing = line.split(';')
print(thing)
print(len(thing))

# the double split pattern
print('the double split pattern:')
line = 'emon hansanbangladeshi'
line1 = line.split()
print(line1)
line2 = line.split('ban')
print(line2)

# python dictionaries
print('python dictionaries:')
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissue'] = 75
print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 2
print(purse)

# comparing lists and dicrionaries
print('comparing list and dictionaries:')
lst = list()
lst.append(21)
lst.append(183)
print(lst)
lst[0] = 23
print(lst)

ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)
ddd['age'] = 23
print(ddd)

# dictionary literls (constants)
print('dictionary  literls (constants)')
jjj = {'chunk':1, 'fred':42, 'jan':100}
print(jjj)

# many counters with a dictionary
print('many counters with a dictionary:')
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['cwen'] = ccc['cwen'] + 1
print(ccc)

# when we see a new name
print('when we see a new name:')
counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
if name in counts:
    counts[name] = counts.get(name, 0) + 1
else:
    x = 0
x = counts.get(name,0)
print(x)

# simplified counting with get()
print('simplified counting with get:')
counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in counts:
    counts[name] = counts.get(name, 0) + 1
print(counts)

# dictionaries and loops
print('dictionaries and loops:')
# counting words and test
# print('counting words and text:')
# count = dict()
# print('enter a line of text:')
# line = input('')
# words = line.split()
# print('words:',words)
# print('counting...')
# for word in words:
#     counts[word] = counts.get(word,0) + 1
# print('counts',counts)

# definite loops and dictionaries
print('definite loops and dictionaries:')
counts = {'chuck':1, 'fred':42, 'jan':100}
for key in counts:
    print(key, counts[key])
    
# retrieving lilsts of keys and values
print('retrieving lilsts of keys and values:')
jjj = {'chuck':1,'fred':52, 'jan':100}
print(list(jjj))
print(jjj.keys())
print(jjj.values())
print(jjj.items())

# rwo iteration variables
print('rwo iteration variables:')
jjj = {'chuck':1, 'fred':42, 'jan':100}
for aaa,bbb in jjj.items():
    print(aaa,bbb)

# the tuples collection
# tuples are like lists
print('tuples are like lists:')
x = ('Glenn', 'Salley', 'Joseph')
print(x[2])

y = (1, 9, 2)
print(y)
print(max(y))

y = (1, 9, 2)
for iter in y:
    print(iter)
    
# a tele of two sequence
print('a tele of two sequence:')
l = list()
print(dir(l))

t = tuple()
print(dir(t))

# tuples and assignment
print('tuples and assignment:')
(x, y) = (4, 'freed')
print(y)

(a, b) = (99, 98)
print(a)

# tuples and dictionaries
print('tuples and dictionaries:')
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
    print(k,v)

tups = d.items()
print(tups)

# tuples are compariable
print('tuples are compariable:')
print((0, 1, 2) < (5, 1, 2))
print((0, 1, 20000000) < (0, 3, 4))
print(('jones', 'sally') < ('jones', 'sam'))
print(('jones', 'salley') > ('adams', 'sam'))

# comparing and sorting tuples
# sorting lists of tuples
print('sorting lists of tuples:')
d = {'a':10, 'b':1, 'c':22}
print(d.items())

d = {'a':10, 'b':1, 'c':22}
print(sorted(d.items()))

d = {'a':10, 'b':1, 'c':22}
for k, v in sorted(d.items()):
    print(k,v)
 
# sort by values instead of key
print('sort by values instead of key:')   
c = {'a':10, 'b':1, 'c':22}
temp = list()
for k, v in c.items():
    temp.append((v,k))
print(temp)

c = {'a':10, 'b':1, 'c':22}
temp = sorted(temp, reverse = True)
print(temp)

# even shorter version
print('even shorter version:')
c = {'a':10, 'b':1, 'c':22}
print(sorted([(v,k) for k,v in c.items()]))
