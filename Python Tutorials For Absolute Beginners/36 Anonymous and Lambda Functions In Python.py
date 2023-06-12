# Anonymous/Lambda Functions In Python
def add(a,b):
    return a - b
print(add(5,2))

# lamda function
minus = lambda x, y: x - y
print(minus(5,2))

def a_first (a):
    return a[1]
a = [[1,14],[0,6],[8,23]]
a.sort(key=a_first)
print(a)

a = [[1,14],[5,6],[8,23]]
a.sort(key=lambda x:x[1])
print(a)
