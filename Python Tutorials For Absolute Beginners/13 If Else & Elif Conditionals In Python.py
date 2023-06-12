# var1 = 6
# var2 = 56
# var3 =  int(input())
# if var3 > var2:
#     print('greater')
# else:
#     print('lesser')
    
list = [5,7,3]
if 5 in list:
    print('yes its in the list')
    
list = [5,7,9]
if 15 not in list:
    print('no its not in the list')
    
print('what is your age?')
age = int(input())
if age < 18:
    print('your cannot drive')
elif age == 18:
    print('we will think about you')
else:
    print('you can drive')

