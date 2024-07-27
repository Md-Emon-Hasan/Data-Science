# loops and list compresion
print("loops and functon:")
planets = ["Mercury", "Venus", "Earth", "Mars", "jupiter", "Saturn", "Neptune"]
for planet in planets:
    print(planet, end=" ")
   
print(" ")
 
multipicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multipicands:
    product = product * mult
print(product)

s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
for char in s:
    if char.isupper():
        print(char, end="")

print(" ")
for i in range(5):
    print("Doing important work. i =", i)
    
# while loops
i = 0
while i < 10:
    print(i, end=" ")
    i += 1

print("")

# list comperehensions
# squares = [n**2 for n in range(10)]
square = [n ** 2 for n in range(10)]
print(square)

for m in range(10):
    square.append(m**2)
print(square)
    
planets = ["Mercury", "Venus", "Earth", "Mars", "jupiter", "Saturn", "Neptune"]
short_planets = [planet for planet in planets if len(planet) < 6]
print(short_planets)

planets = ["Mercury", "Venus", "Earth", "Mars", "jupiter", "Saturn", "Neptune"]
loud_short_planets = [planet.upper() + "!" for planet in planets if len(planet) < 6]
print(loud_short_planets)

def count_negatives(nums):
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negetive = n_negative + 1
        return n_negative
print(count_negatives([5, -1, -2, 0, 3]))

