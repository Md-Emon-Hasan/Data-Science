# regular expression
print('regular expression:')
hand  = open('firstfile.txt')
for line in hand:
    line = line.rstrip()
    if line.find('bangladesh') >= 0:
        print(line)
    
import re
hand = open('firstfile.txt')
for line in hand:
    line = line.rstrip()
    if re.search('bangladesh', line):
        print(line)
        
# using re.search() like startswith()
print('using re.search() like startwith():')
hand = open('firstfile.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('bangladesh'):
        print(line)

import re
hand = open('firstfile.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^bangladesh', line):
        print(line)

# matching and extracting data
print('matching and extraching data:')
import re
x = 'my 2 favourite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)

x = 'hello 5465 hfdas 45 gsa 52 74 54165 466 shakil'
y = re.findall('[0-9]+', x)
print(y)

x = 'bangladesh'
y = re.findall('[aeiou]+',x)
print(y)

# warning: greedy matching
print('warning: greedy matching:')
import re
x = 'From: Using the: character'
y = re.findall('^F.+:', x)
print(y)

# non greedy matching
print('non greedy matching:')
import re
x = 'From: Using the : character'
y = re.findall('^F.+?:',x)
print(y)

# regular expression practical application
print('regular expression practical application:')
data = 'From stephen.marqured@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ',atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)

# the regex version
print('the regex version:')
data = 'From stephen.marqured@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('@([^ ]*)',data)
print(y)

# even cooler regex version
print('even cooler regex version:')
data = 'From stephen.marqured@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('^From .*@([^ ]*)',data)
print(y)

import re
hand = open('firstfile.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('([0-9.]+)',line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))

# excape character
print('excape character:')
import re
x = 'we just received $10.00 for cookies.'
y = re.findall('\$[0-9]+',x)
print(y)

# sockets in python
print('sockets in python:')
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
print(mysock)

# networking protocol
# internet standards

# network write a web browser
print('networking write web browser:')
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'Get http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

# networking text processing
# about characters and string...
# representing simplw string
print('representing simple string:')
print(ord('H'))
print(ord('e'))
print(ord('\n'))

# python string to bytes
print('python string to bytes:')
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'Get http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

# networking using urllib in python
print('networking using urllib in python:')
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
    
# using urllab like a file
print('using urllab like a file:')
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

# reading web pages
# print('reading web pages:')
# import urllib.request, urllib.parse, urllib.error
# fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.html')
# for line in fhand:
#     print(line.decode().strip())
    
# following links
# print('following links:')
# import urllib.request, urllib.parse, urllib.error
# fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.html')
# for line in fhand:
#     print(line.decode().strip())

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# url = input('Enter - ')
# html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html, 'html.parser')
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href',None))

# XML basics
print('XML basics')

    