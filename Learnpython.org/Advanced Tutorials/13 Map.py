# map 
my_pets = ["alfred", "tabitha", "william", "arla"]
uppered_pets = []
for pet in my_pets:
    pet_ = pet.upper()
    uppered_pets.append(pet_)
print(uppered_pets)

my_pets = ["alferd", "tabitha", "william", "arla"]
uppered_pets = list(map(str.upper, my_pets))
print(uppered_pets)

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
result = list(map(round, circle_areas, range(1, 7)))
print(result)

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 32.00013]
result = list(map(round, circle_areas, range(1, 3)))
print(result)

my_string = ["a", "b", "c", "d", "e"]
my_numbers = [1, 2, 3, 4, 5]
result = list(zip(my_string, my_numbers))
print(result)

my_string = ["a", "b", "c", "d", "e"]
my_numbers = [1, 2, 3, 4, 5]
results = list(map(lambda x,y: (x, y), my_string, my_numbers))
print(results)

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
def is_A_student(score):
    return score > 75
over_75 = list(filter(is_A_student, scores))
print(over_75)

dromes = ("demigd", "rewire", "madam", "freer", "anutforajaroftuna", "kisok")
palindroms = list(filter(lambda word: word == word[::-1], dromes))
print(palindroms)

from functools import reduce
numbers = [3, 4, 6, 9, 34, 12]
def custom_sum(first, second):
    return first + second
result = reduce(custom_sum, numbers)
print(result)

from functools import reduce
numbers = [3, 4, 6, 9, 34, 12]
def custom_sum(first, second):
    return first + second
result = reduce(custom_sum, numbers, 10)
print(result)

# example
from functools import reduce
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
my_names = ["olumide", "akinremi", "joiah", "temidayo", "omoseun"]
my_numbers = [4, 6, 9, 23, 5]
map_result = list(map(lambda x: round(x ** 2, 3), my_floats))
filter_result = list(filter(lambda name: len(name) <= 7, my_names))
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)
print(map_result)
print(filter_result)
print(reduce_result)
