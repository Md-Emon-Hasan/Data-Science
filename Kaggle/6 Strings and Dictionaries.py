# Strings and Dictionaries
print("string and dictionaries:")
x = "Pluto is a planet"
y = "Pluto is a planet"
print(x == y)

print("Pluto is a planet")
print("My dog is named 'Pluto'")

print("Pluto\"s a planet!")

print("hello\nworld")

triplequoted_hello = """hello world"""
print(triplequoted_hello)

print("hello")
print("world")
print("hello", end="")
print("pluto", end="")

print("")

# string sequence
print("string are sequence:")
planet = "Pluto"
print(planet[0])

planet = "Pluto"
print(planet[-3:])

planet = "Pluto"
print(len(planet))

planet = "Pluto"
print([char + "! " for char in planet])

# string methods
print("strings methods:")
claim = "Pluto is a planet!"
print(claim.upper())

claim = "Pluto is a planet!"
print(claim.lower)

claim = "Pluto is a planet!"
print(claim.index("plan"))

claim = "Pluto is a planet!"
print(claim.startswith(planet))

claim = "Pluto is a planet!"
print(claim.endswith("planet"))

# going between strings and lists:
print("Going between strings and lists:")
claim = "Pluto is a planet"
print(claim.split())

datestr = "1956-01-31"
print(datestr.split("-"))

# Building strings with
planet = "Pluto"
print(planet +", we miss you")

planet = "Pluto"
position = 9
planet + ", you'll always be the " + str(position) + "th planet to me."

# dictionaries
number = {
    "one" : 1,
    "two" : 2,
    "three" : 3
}
print(number)

number = {
    "one" : 1,
    "two" : 2,
    "three" : 3
}
print(number["one"])

number = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "eleven" : 11
}
print(number)

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial)

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print('Saturn' in planet_to_initial)
print('Betelgeuse' in planet_to_initial)

