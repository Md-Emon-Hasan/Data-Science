# Map, Filter & Reduce

# normal method
numbers = ['3','34','64']
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
hello = numbers[2] + 1
print(hello)

# map with function
def sq(a):
    return a * a
num = [2,3,6,6,7,6,3,3,2]
square = list(map(sq, num))
print(square)

# map with function
num = [2,3,6,6,7,6,3,3,2]
square = list(map(lambda x: x*x, num))
print(square)

def square(a):
    return a * a
def cube1(a):
    return a * a * a
func = [square, cube1]
for i in range(5):
    val = list(map(lambda x:x(i), func))
    print(val)
    
# filter
num = [2,3,6,6,7,6,3,3,2]
def is_greater_5(num):
    return num > 5
gr_then_5 = list(filter(is_greater_5,num))
print(gr_then_5)

# reduce 
from functools import reduce
list1 = [1,2,3,4]
num = 0
for i in list1:
    num = num + i
print(num)

list1 = [1,2,3,4,7]
num = reduce(lambda x,y:x+y, list1)
print(num)

list1 = [1,2,3,4,7]
num = reduce(lambda x,y:x*y, list1)
print(num)
