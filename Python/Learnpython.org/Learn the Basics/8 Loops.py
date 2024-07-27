# for loops
print("for loops:")
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

# for loops
print("for loops:")
for x in range (5):
    print(x)

print("loops:")
for x in range(3, 6):
    print(x)

print("loops:")
for x in range(3, 8, 2):
    print(x)

# while loop
count = 0
while count < 5:
    print(count)
    count += 1

# using loop with break and countinue statement
print("using loop with break and countinue statement:")
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Check if x is even
print("Check if x is even:")
for x in range(10):
    if x % 2 == 0:
        continue
    print(x)

# Check if x is odd
print("Check if x is odd:")
for x in range(10):
    if x % 2 == 0:
        print(x)
        
count = 0
while(count < 5):
    print(count)
    count += 1
else:
    print("count value reached %d" %(count))

for i in range(1, 10):
    if(i % 5 == 0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")

# example
print("example:")
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]
for number in numbers:
    if number == 237:
        break
    if number % 3 == 1:
        continue
    print(number)

