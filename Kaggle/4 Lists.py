# list
print("list:")
primes = [2, 3, 5, 7]
print(primes)

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Uranus", "Neptune"]
print(planets)

hands = [
    ["J", "Q", "K"],
    ["2", "2", "2"],
    ["6", "A", "K"]
]
print(hands)

hands = [["J", "Q", "K"], ["2", "2", "2"], ["6", "A", "K"]]
print(hands)

my_favourite_things = [32, "raindrops on roses", help]
print(my_favourite_things)

# slicing
print("slicing:")
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Uranus", "Neptune"]
print(planets[0])
print(planets[0:3])
print(planets[:3])
print(planets[3:])
print(planets[1:-1])
print(planets[1:-1])
print(planets[-3:])
print(planets[1])
print(planets[-1])
print(planets[-2])

# changing lists
print("chinging lists:")
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Uranus", "Neptune"]
planets[3] = "Malacandra"
print(planets)

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Uranus", "Neptune"]
planets[:3] = ["Mur", "Vee", "Ur"]
print(planets)

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Uranus", "Neptune"]
planets[:4] = ["Mercury", "Venus", "Earth", "Mars"]
print(planets)

# list function
print("list function:")
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Uranus", "Neptune"]
print(len(planets))

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Uranus", "Neptune"]
print(sorted(planets))

# sum of all number
primes = [2, 3, 5, 7]
print(sum(primes))

# find max number
primes = [2, 3, 5, 7]
print(max(primes))

# real number
x = 12
print(x.imag)

x = 12 + 3j
print(x.imag)

# list methods
print("list function:")

# use append function
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Uranus", "Neptune"]
hello = planets.append("pluto")
print(hello)

# use pop for remove last element
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Uranus", "Neptune"]
print(planets.pop())

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Uranus", "Neptune"]
hello = planets.index("Earth")
print(hello)

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Uranus", "Neptune"]
for x in planets:
    print(x)
    
# tuples
print("tuples:")
t = (1, 2, 3)
print(t)

x = 0.125
print(x)
print(x.as_integer_ratio())

# swapping variables
a = 1
b = 0
a, b = b, a
print(a, b)
