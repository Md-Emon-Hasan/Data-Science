# closure

# closure with nested function
print("closure nested function:")
print("closures:")
def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)
    data_transmitter()
print(transmit_to_space("Text message"))

def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        nonlocal number
        number = 3
        print(number)
    printer()
    print(number)
print_msg(9)

def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)
        return data_transmitter

def multiplier_of(n):
    def multiplier(number):
        return number * 2
    return multiplier
multiplaywith5 = multiplier_of(5)
print(multiplaywith5(9))

