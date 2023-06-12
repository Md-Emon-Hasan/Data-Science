# booleans and conditions
print("booleans and conditons:")
x = True
print(x)
print(type(x))

# comparison operator
print("comparison operator:")
def can_run_president(age):
    return age >= 35
print("Can a 19-years-old run for president(19)")
print("Can a 45-year-old run for president(45)")

def is_odd(n):
    return (n % 2) == 1
print("Is 100 odd?", is_odd(100))
print("Is -1 odd", is_odd(-1))

def can_run_for_president(age, is_natural_born_citizen):
    return is_natural_born_citizen and (age >= 35)
print(can_run_for_president(19, True))
print(can_run_for_president(55, False))
print(can_run_for_president(55, True))

def inspect(x):
    if x == 0:
        print(x, "is xero")
    elif x > 0:
        print(x, "is posetive")
    elif x < 0:
        print(x, "is negetive")
    else:
        print(x, "is unlike anything I've ever see n...")
inspect(10)      

def f(x):
    if x > 0:
        print("Only printed when x is positive value x = ", x)
        print("Also only printed when x is posetive = x", x)
    print("Always printed, regardless of x's value; x =", x)
f(1)
f(0)

# Boolean conversion
print("Boolean conversion:")
print(bool(1))
print(bool(0))
print(bool("asf"))
print(bool(""))

if 0:
    print(0)
elif "spam":
    print("spam")

def is_hello(w):
    return ("hello emon " + w)
print(is_hello("hasan"))
