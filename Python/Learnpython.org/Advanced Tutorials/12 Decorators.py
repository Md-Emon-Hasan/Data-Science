# decorators
print("decorators:")

# @decorator
# def function(arg):
#     return "value"

# def function(arg):
#     return = "value"
# function = decorator(function)

def repeater(old_function):
    def new_function(*args, **kwds):
        old_function(*args, **kwds)
        old_function(*args, **kwds)
    return new_function

def double_out(old_function):
    def new_function(*args, **kwds):
        return 2 * old_function(*args, **kwds)
    return new_function

def double_Ii(old_function):
    def new_function(arg):
        return old_function(arg * 2)
    return new_function

def check(old_function):
    def new_function(arg):
        if arg < 0: raise(ValueError, "Negetive Argument")
        old_function(arg)
    return new_function

def multiply(multiplier):
    def multiply_generator(old_function):
        def new_function(*args, **kwds):
            return multiplier * old_function(*args, **kwds)
        return new_function
    return multiply_generator
@multiply(3)
def return_num(num):
    return num
return_num(5)

def type_check(correct_type):
    def check(old_function):
        def new_function(arg):
            if (isinstance(arg, correct_type)):
                return old_function(arg)
            else:
                print("Bad Type")
        return new_function
    return check
@type_check(int)
def times2(num):
    return num * 2
print(times2(2))
times2("Not A Number")
@type_check(str)
def first_letter(word):
    return word[0]
print(first_letter("Hello World"))
first_letter(["Not", "A", "Strong"])
