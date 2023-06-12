# for loop
for letter in "Bangladesh":
    print(letter)

friends = ["Jim", "Karan", "Kevin"]
for friend in friends:
    print(friend)

# for loop with range
for index in range(10):
    print(index)

print("End the loop")

for index in range(3, 10):
    print(index)

print("End the loop")

friends = ["Jim", "Karan", "Kevin"]
for index in range(len(friends)):
    print(index)
    
print("End the loop")

for index in range(5):
    if index == 0:
        print("first interation")
    else:
        print("Not first")
