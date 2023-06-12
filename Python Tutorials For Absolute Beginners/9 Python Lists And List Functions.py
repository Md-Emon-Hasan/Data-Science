# Python Lists And List Functions
grocery = ['harpic', 'vim var', 'deodrant', 'bhindi', 56]
print(grocery)

grocery = ['harpic', 'vim var', 'deodrant', 'bhindi', 56]
print(grocery[1])

numbers = [2,7,9,11,3]
print(numbers)

numbers = [2,7,9,11,3]
print(numbers[2])

numbers = [2,7,9,11,3]
numbers.sort()
print(numbers)

numbers = [2,7,9,11,3]
numbers.reverse()
print(numbers)

numbers = [2,7,9,11,3]
print(numbers[0:5])
print(numbers[:])
print(numbers[1:4])
print(numbers[::1])
print(numbers[::3])
print(numbers[::-1])

numbers = []
numbers.append(1)
numbers.append(72)
numbers.append(5)
print(numbers)

# insert
numbers = []
numbers.insert(1, 67)
print(numbers)

# remove
numbers = [2,7,9,11,3]
numbers.remove(9)
print(numbers)

# pop for remove last element
numbers = [2,7,9,11,3]
numbers.pop()
print(numbers)

# tuples
tp = (1)
print(tp)

a = 1
b = 8
temp = a
a = b
b = temp
print(a, b)