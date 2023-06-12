# Classes and Objects
print("Classes and Objects:")
class MyClass:
    variable = "blah"

class MyClass:
    variable = "blah"
myobject = MyClass()

class MyClass:
    variable = "blah"
myobject = MyClass()
myobject.variable

class MyClass:
    variable = "blah"
myobject = MyClass()
print(myobject.variable)

class MyClass:
    variable = "blah"
myobject = MyClass()
myobject = MyClass()
myobject.variable = "yackity"
print(myobject.variable)
print(myobject.variable)

class MyClass:
    a = "hello"
    b = "world"
c = MyClass()
print(c.a)
print(c.b)

# Accessing Object Functions
print("Accessing Object Functions:")
class MyClass:
    variable = "blah"
    def function(self):
        print("This is a message inside the class.")
myobjectx = MyClass()
myobjectx.function()

# init()
print("init():")
class NumberHolder:
   def __init__(self, number):
       self.number = number
   def returnNumber(self):
       return self.number
var = NumberHolder(7)
print(var.returnNumber())

# exercise
print("exercise:")
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00
car2 = Vehicle()
car2.name = "Jump"

