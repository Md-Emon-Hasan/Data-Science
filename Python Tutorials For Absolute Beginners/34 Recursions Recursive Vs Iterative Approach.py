# Recursions: Recursive Vs Iterative Approach
def print2(str1):
    print('This is ' + str1)
print2('harry')

# Iterative
def factorial(n):
    fac = 1
    for i in range(n):
        fac = fac * (i + 1)
    return fac
# number = int(input('Enter then number'))
print(factorial(5))

# recursive
def factorial1(n):
    if n == 1:
        return 1
    else:
        return n * factorial1(n - 1)
print(factorial1(5))

def fibonacci1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci1(n - 1) + fibonacci1(n - 2)
print(fibonacci1(6)) 

