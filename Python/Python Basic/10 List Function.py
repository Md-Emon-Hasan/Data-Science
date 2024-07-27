# using extend function
lucky_numbers = [1, 2, 3, 4, 5]
friends = ["Kevin", "Karan", "Jim", "Oscar", "Toby"]
lucky_numbers.extend(friends)
print(lucky_numbers)

# using append function
friends = ["Kevin", "Karan", "Jim", "Oscar", "Toby"]
friends.append("Emon")
print(friends)

# using insert function
friends = ["Kevin", "Karan", "Jim", "Oscar", "Toby"]
friends.insert(1, "Emon")
print(friends)

# using remove function
friends = ["Kevin", "Karan", "Jim", "Oscar", "Toby"]
friends.remove("Karan")
print(friends)

# using clear function
friends = ["Kevin", "Karan", "Jim", "Oscar", "Toby"]
friends.clear()
print(friends)

# using pop function
# pop function use for remove last element
friends = ["Kevin", "Karan", "Jim", "Oscar", "Toby"]
friends.pop()
print(friends)

# finding index value
friends = ["Kevin", "Karan", "Jim", "Oscar", "Toby"]
print(friends.index("Karan"))

# count element
friends = ["Kevin", "Karan", "Jim", "Jim", "Oscar", "Toby"]
print(friends.count("Jim"))

# using short function for assendeing element
friends = ["Kevin", "Karan", "Jim", "Jim", "Oscar", "Toby"]
friends.sort()
print(friends)

friends = [12, 8, 9, 6, 15]
friends.sort()
print(friends)

# using copy function for copy one to another
friends = ["Kevin", "Karan", "Jim", "Jim", "Oscar", "Toby"]
friends1 = friends.copy()
print(friends1)
