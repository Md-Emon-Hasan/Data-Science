# String Formatting
print("String Formatting:")
name = "John"
print("Hello, %s!" % name)

# use multiple string
name = "John"
age = 23
print("%s is %d years old." % (name, age))

# print with list
print("print with list:")
mylist = [1, 2, 3]
print("A list: %s" % mylist)

# erercise
print("exercise:")
data = ("john", "Doe", 53.54)
format_string = "Hello %s %s. Your current balance is $%s."
print(format_string % data)
