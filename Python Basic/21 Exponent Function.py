# exponent function
from unittest import result

print(2 ** 3)

def rise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
print(rise_to_power(3, 4))
