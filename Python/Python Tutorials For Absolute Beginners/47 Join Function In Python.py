# Join Function In Python
# normal
lis = ['john','cena','randy','orton','shemus','khali','jindar']
for item in lis:
    print(item)
print('other wwe superstar')

# join
lis = ['john','cena','randy','orton','shemus','khali','jindar']
for item in lis:
    print(item,'and',end=' ')
print('other wwe superstar')

# join function
lis = ['john','cena','randy','orton','shemus','khali','jindar']
a = ' and '.join(lis)
print(a, 'other wwe superstar')

lis = ['john','cena','randy','orton','shemus','khali','jindar']
a = ', '.join(lis)
print(a, 'other wwe superstar')
