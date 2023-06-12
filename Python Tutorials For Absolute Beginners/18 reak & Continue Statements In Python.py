# break statement
i = 0
while True:
    print(i + 1, end=' ')
    if(i == 44):
        break
    i = i + 1

i = 0
while True:
    if i + 1 < 5:
        continue
    print(i + 1, end=' ')
    if(i == 44):
        break
    i = i + 1
    
# while True:
#     inp = int(input('enter a number:'))
#     if inp > 100:
#         print("you win")
#         break
#     else:
#         print('try again')
#         continue
    