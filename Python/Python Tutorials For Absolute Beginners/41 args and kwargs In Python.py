# *args and **kwargs In Python
def function_name_print(a,b,c,d,e):
    print(a,b,c,d,e)
function_name_print('harry','rohan','skillf','hammad','shiva')

def funargs(*args):
    print(type(args))
    print(args[0])
har = ['harry','rohan','skillf','hammad','shiva']
funargs(*har)

def funargs(normal, *args):
    print('noraml')
    for item in args:
        print(item)
har = ['harry','rohan','skillf','hammad','shiva']
normal = 'i am a students'
funargs(normal,*har)

def funargs(normal, *args, **kwargs):
    print('noraml')
    for item in args:
        print(item)
    for key, value in kwargs.items():
        print(key, value)
har = ['harry','rohan','skillf','hammad','shiva']
mar = {'harry':'abc1','rohan':'abc2','skillf':'abc3','hammad':'abc4','shiva':'abc5'}
normal = 'i am a students'
funargs(normal,*har, **mar)
