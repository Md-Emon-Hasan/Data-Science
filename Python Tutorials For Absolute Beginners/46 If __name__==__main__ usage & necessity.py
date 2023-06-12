# 46 If __name__==__main__ usage & necessity
def printhar(string):
    return "ye string harry ko de do", string
def add(num1, num2):
    return num1 + num2 + 5
print(printhar('harry1'))
o = add(4,6)
print(o)
print(add(5,3))

if __name__ == '__main__':
    print(printhar('harry1'))
    o = add(4,6)
    print(o)
    
print('and the name is',__name__)
if __name__ == '__main__':
    print(printhar('harry1'))
    o = add(4,6)
    print(o)
