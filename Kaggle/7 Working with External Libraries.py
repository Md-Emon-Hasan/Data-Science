# working with external libraries
print("working with external libraries:")
import math
print("IT's math! It has type{}".format(type(math)))

print(dir(math))

print("pi to 4 significiant digits = {:.4}".format(math.pi))

print(format(math.pi))

# other import syntex
print("other import syntex:")
import math as mt
print(mt.pi)

from math import *
print(pi, log(32, 2))

# impoort numpy
print("import numpy:")
import numpy
print("numpy.random is a", type(numpy.random))
print("it contains names such as...", dir(numpy.random)[-15])

# roll dice
print("roll dice:")
rolls = numpy.random.randint(low=1, high=6, size=10)
print(rolls)

rolls = numpy.random.randint(low=1, high=6, size=10)
print(type(rolls))

rolls = numpy.random.randint(low=1, high=6, size=10)
print(dir(rolls))

rolls = numpy.random.randint(low=1, high=6, size=10)
print(rolls.mean())

rolls = numpy.random.randint(low=1, high=6, size=10)
print(rolls.tolist())

rolls = numpy.random.randint(low=1, high=6, size=10) + 10
print(rolls)

rolls = numpy.random.randint(low=1, high=6, size=10) <= 3
print(rolls)

xlist = [[1,2,3],[4,5,6],]
x = numpy.asarray(xlist)
print("xlilst = {}\nx =\n{}".format(xlist, x))

