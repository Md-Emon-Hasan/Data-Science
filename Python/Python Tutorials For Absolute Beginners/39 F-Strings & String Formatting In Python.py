# F-Strings & String Formatting In Python
me = "Harry"
a = 'this is %s'%me
print(a)

# me = 'harry'
# a1 = 3
# a = 'this is %s %s'(me,a1)
# print(a)

me = 'harry'
a1 = 3
a = 'this is {} {}'
b = a.format(me, a1)
print(b)

me = 'harry'
a1 = 3
a = 'this is {1} {0}'
b = a.format(me, a1)
print(b)

me = 'harry'
a1 = 3
a = f'this is {me} {a1}'
print(a)

me = 'harry'
a1 = 3
a = f'this is {me} {a1} {4*65}'
print(a)

import math
me = 'harry'
a1 = 3
a = f'this is {me} {a1} {math.cos(65)}'
print(a)
