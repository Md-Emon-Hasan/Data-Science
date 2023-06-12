# partial function
print("partial function:")
from functools import partial
def multyply(x,y):
    return x * y
dbl = partial(multyply, 2)
print(dbl(4))

# exercise
print("exercise:")
from functools import partial
def func(u, v, w, x):
    return u * 4 + v * 3 + w * 2 + x
p = partial(func, 5, 6, 7)
print(p(8))
