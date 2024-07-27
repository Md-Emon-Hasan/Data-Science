# print hello world
print("hello world")

# Drawing a Shape
print("     /|")
print("    / |")
print("   /  |")
print("  /   |")
print(" /    |")
print("/_____|")

# declearing variables
character_name = "emon"
character_age = "20"
print("My name is " + character_name + ", I am " + character_age + " years old")

# working with string
print("Giraffe Academy")
print("Giraffe\nAcademy")
print("Giraffe \" Academy")

phrase = "Giraffe Academy"
print(phrase)
# lowercase
print(phrase.lower())
# uppercase
print(phrase.upper())
# check upper case
print(phrase.isupper())
print(phrase.upper().isupper())
# check len
print(len(phrase))
# index value
print(phrase[0])
# index character value
print(phrase.index("G"))
# replace string
print(phrase.replace("Giraffe", "Elephant"))

# working with number
print(120)
print(12.325654859)
print(-6.165444469)
print(3 + 3)
print(3 + 2.5)
print(3 - 2.5)
print(3 * 2.5)
print(3 / 2.5)
print(10 % 3)
print(3 * (4 + 5))

my_num = 5
print(str(my_num) + " this is my favourite number")
# negetive value to posetive
my_num = -5
print(my_num)
print(abs(my_num))
# power value
print(pow(3,2))
# round function
print(round(3.56))
from ast import If, Num
from functools import total_ordering
from gettext import translation
from math import *
import re
# without decimal value 
print(floor(3.444))
print(ceil(4.02))
# finding square root
print(sqrt(36))

# getting input from users
'''
name = input("Enter your name: ")
print("Hello " + name + "!")

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! are you " + age + "!" )
'''
# building a basic calculator
'''
num1 = input("Enter first number: ")
num2 = input("Enter Second number: ")
total = float(num1) + float(num2)
print(total)
'''
# buliding a md libs game
'''
flower = input("Enter a flower name: ")
color = input("Enter a color name: ")
person = input("Enter a person name: ")

print(flower + " is your favourite flower")
print(color + " is your favourite color")
print(person + " is your favourite person")
'''

# list
friends = ["kevin", "karan", "jim", "oscar", "toby"]
print(friends)
# index value
print(friends[0])
# index negetive value
print(friends[-1])
# contains value
print(friends[1:3])
print(friends[0:1])
# value change
friends = ["kevin", "karan", "jim", "oscar", "toby"]
friends[1] = "Mike"
print(friends)

# list function
# extend function
lucky_number = [4, 8, 15, 16, 23, 42]
friends = ["kevin", "karan", "jim", "oscar", "toby"]
friends.extend(lucky_number)
print(friends)
# append function
friends = ["kevin", "karan", "jim", "oscar", "toby"]
friends.append("Creed")
print(friends)
# insert function
friends = ["kevin", "karan", "jim", "oscar", "toby"]
friends.insert(1, "kelly")
print(friends)
# remove function
friends = ["kevin", "karan", "jim", "oscar", "toby"]
friends.remove("oscar")
print(friends)
# clear function
friends = ["kevin", "karan", "jim", "oscar", "toby"]
friends.clear()
print(friends)
# clear last list
friends = ["kevin", "karan", "jim", "oscar", "toby"]
friends.pop()
print(friends)
# find with index value
friends = ["kevin", "karan", "jim", "oscar", "toby"]
print(friends.index("oscar"))
# shorting list
lucky_number = [42, 8, 15, 16, 23]
lucky_number.sort()
print(lucky_number)
# reverse list
lucky_number = [42, 8, 15, 16, 23]
lucky_number.reverse()
print(lucky_number)
# copy function
lucky_number = [42, 8, 15, 16, 23]
lucky_number1 = lucky_number.copy()
print(lucky_number1)

# tuples
coordinates = (4, 5)
print(coordinates[1])
coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]
print(coordinates[2])

# function
def sayhi():
    print("hello user")
sayhi()

def sayhi():
    print("hello user")
print("Top")
sayhi()
print("bottom")

def sayhi(name):
    print("hello " + name)
sayhi("emon")
sayhi("hasan")

def sayhi(name, age):
    print("hello " + name + "! you are " + age + "!")
sayhi("emon", "20")
sayhi("hasan", "20")

# return statement
def cube(num):
    return num * num * num
print(cube(3))

def cube(num):
    return num * num * num
result = cube(4)
print(result)

# is statement
is_male = False
if is_male:
    print("You are not a male")
else:
    print("You are a male")
    
is_male = True
if is_male:
    print("You are a male")
else:
    print("You are not a male")

is_male = True
is_tall = False
if is_male or is_tall:
    print("you are a male or tall or both")
else:
    print("you are neither male or tall")
    
is_male = False
is_tall = False
if is_male or is_tall:
    print("you are a male or tall or both")
else:
    print("you are neither male or tall")
    
is_male = True
is_tall = True
if is_male or is_tall:
    print("you are a male or tall or both")
else:
    print("you are neither male or tall")
    
is_male = True
is_tall = False
if is_male and is_tall:
    print("you are a male or tall or both")
elif is_male and not is_tall:
    print("you are short male")
else:
    print("you are neither male or tall")
    
is_male = False
is_tall = True
if is_male and is_tall:
    print("you are a male or tall or both")
elif is_male and not is_tall:
    print("you are short male")
elif not is_male and is_tall:
    print("you are not a male but a tall")
else:
    print("you are neither male or tall")
    
# if statements and comparisons
def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3
print(max_num(3, 4, 5))

# building a better calculator
'''
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter any operator: ")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("invalid oprator")
'''

# dictionaries
monthConversions ={
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
    "Dec" : "December"
}
print(monthConversions["Feb"])
print(monthConversions.get("Dec"))
print(monthConversions.get("love"))
print(monthConversions.get("love", "Not a valid input"))

# while loop
i = 1
while i < 5:
    print(i)
    i += 1
print("End while loop")

# guessing game
'''
secret_word = "emon"
guess = ""

while secret_word != guess:
    guess = input("enter guessing word: ")
print("you win")
'''

'''
secret_word = "emon"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False

while guess != secret_word and not out_of_guess:
    if guess_count < guess_limit:
        guess = input("guess a world: ")
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess:
    print("out of guesses, You Lose!")
else:
    print("Yiu win")
'''

# for loop
for letter in "Giraffe Academy":
    print(letter)
    
friends = ["jim", "karan", "kevin"]
for friend in friends:
    print(friend)

for index in range(10):
    print(index)
    
for index in range(3, 5):
    print(index)
    
friends = ["jim", "karan", "kevin"]
for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("First Interation")
    else:
        print("Not First")

# exponent function
print(2 ** 3)

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
print(raise_to_power(2, 5))

# 2D lists & nested loop
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(number_grid[0][0])
print(number_grid[1][2])

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
for index in number_grid:
    print(index)

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
for index in number_grid:
    for index1 in index:
        print(index1)
        
# building a translator
'''
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter any word: ")))
      
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.islower():
                translation = translation + "g"
            else:
                translation = translation + "G"
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter any word: ")))
'''

# comment
# this is comment
'''
this is another type comment
'''

# try/except
# try:
#     number = int(input("enter a number: "))
#     print(number)
# except:
#     print("invalid input")

try:
    value = 10/0
except:
    print("invalid input")
    
try:
    value = 10/0
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("invalid input")

try:
    value = 10/0
except ZeroDivisionError as ErrorFirst:
    print(ErrorFirst)
except ValueError as ErrorLast:
    print(ErrorLast)
    
# reading files
# we can only read this files
open("employees.txt", "r")
# we can change the filse
open("employees.txt", "w")
# we can add new information and more
open("employees.txt", "a")
# we can ewad and write the files
open("employees.txt", "r+")

'''
employee_file = open("employees.txt", "r")
print(employee_file.readable())
employee_file.close()
# for reading first line
employee_file = open("employees.txt", "r")
print(employee_file.readline())
print(employee_file.readline())
employee_file.close()
# for reading each lines
# employee_file = open("employees.txt", "r")
# print(employee_file.readlines())
# employee_file.close()

# mployee_file = open("employees.txt", "r")
# for employee in employee_file.readlines():
#     print(employee)
# employee_file.close()

# writing files
# employee_file = open("employees.txt", "r")
# print(employee_file.read())
# employee_file.close()

# employee_file = open("employees.txt", "a")
# employee_file.write("Toby - Human Resources")
# employee_file.close()

# employee_file = open("employees.txt", "w")
# employee_file.write("Toby - Human Resources")
# employee_file.close()

# employee_file = open("index.html", "w")
# employee_file.write("<p>this is html</p>")
# employee_file.close()
'''

# building a multiple choice quiz
