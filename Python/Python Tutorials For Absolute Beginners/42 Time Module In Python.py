# Time Module In Python
import time
initial = time.time()

k = 0
while (k < 45):
    print('this is hasan')
    k +=1
print('while loop run in', time.time() - initial, 'seconds')

# with sleeping function 
# k = 0
# while (k < 45):
#     print('this is hasan')
#     time.sleep(2)
#     k +=1
# print('while loop run in', time.time() - initial, 'seconds') 

initial2 = time.time()   
for i in range(45):
    print('this is emon')
print('for loop run in', time.time() - initial2, 'seconds')

# local time
localtime = time.asctime(time.localtime(time.time()))
print(localtime)
