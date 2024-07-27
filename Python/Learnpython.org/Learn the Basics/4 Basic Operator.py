# basic operator
# arithmetic operator
print("arithmetic operator:")
number = 1 + 2 * 3 / 4.0
print(number)

# % or remainder operator
print("% or remainder operator:")
reminder = 11 % 3
print(reminder)

# Using two multiplication symbols makes a power relationship
print("Using two multiplication symbols makes a power relationship:")
squered = 7 ** 2
print(squered)
cubed = 2 ** 3
print(cubed)

# using operator with string
print("using operator with string:")
helloworld = "hello" + " " + "world"
print(helloworld)

# multiplying strings
print("multiplying strings:")
lostofhellos = "hello " * 10
print(lostofhellos)

print([1, 2, 3] * 3)

# Using Operators with Lists
print("Using Operators with Lists:")
even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

# erercise
print("exercise:")
x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

if x_list.count(x) == 0 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
