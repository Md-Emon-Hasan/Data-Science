# global variable
l = 10 # global
def function1(n):
    l = 5
    print(n, 'I have printed')
function1('This is me')
print(l)

# local variable
l = 10
def function1(n):
    l = 5 # local
    m = 8 # local
    print(l, m)
    print(n, 'I have printed')
function1('This is me')
print(l)

def harry():
    x = 20
    def rohan():
        global x
        x = 88
    print('before calling rohan()', x)
    rohan()
    print('after calling rohan', x)
harry()
print(x)

# Recursions: Recursive Vs Iterative Approach
