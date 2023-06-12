# Enumerate Function
# l1 = ['bhindi','aloo','chopsticks','chowmein']
# i = 1
# for item in l1:
#     if i%2 is not 0:
#         print(f"{item}")
#     i += 1

l1 = ['bhindi','aloo','chopsticks','chowmein']
for index, item in enumerate(l1):
    if index%2 == 0:
        print("jarvis please buy", item)
        