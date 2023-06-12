# function
print("function:")
def my_function():
    print("Hello From My Function")
my_function()

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function, I wish you %s" % (username, greeting))
my_function_with_args("emon", 21)

# function with arguments
print("function with arguments:")
def sum_two_numbers(a, b):
    print(a + b)
sum_two_numbers(10, 20)

# exercise
print("exercise:")
def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()