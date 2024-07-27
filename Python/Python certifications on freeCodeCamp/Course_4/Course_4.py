# python object
# objects: A sample class
print('objects: a sample class:')
class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x + 1
        print('So fair',self.x)
an = PartyAnimal()
an.party()
an.party()
an.party()

# playing dir and type
print('playing dir and type:')
x = list()
print(type(x))
print(dir(x))

# try dir with string
print('try dir with a string:')
y = "Hello there"
print(dir(y))

class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x + 1
        print('So far', self.x)
an = PartyAnimal()
print('Type', type(an))
print('Dir', dir(an))

# object lifecycle
print('object lifecycle:')
class PartyAnimal1:
    def __init__(self):
        print('Hello i am Emon')
    x = 19
    def name1(self):
        self.x = self.x + 1
        print('I am ',self.x)
an = PartyAnimal1()
an.name1()

class PartyAnimal:
    x = 0
    def __init__(self):
        print('I am constructed')
    def party(self):
        self.x = self.x + 1
        print('So far',self.x)
    def __del__(self):
        print('I am destructed',self.x)
an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains',an)

print('New object:')
class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, z):
        self.name = z
        print(self.name,'constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name,'party count',self.x)
s = PartyAnimal('Sally')
s.party()
j = PartyAnimal('Jim')
j.party()
s.party()

# Inheritance
print('inheritance:')
# terminology: inheritance
print('terminal: inheritance:')
class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name,'constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name,'party count',self.x)
class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name,'points',self.points)
s = PartyAnimal('Sally')
s.party
j = FootballFan('Jim')
j.party()
j.touchdown()
