# Dictionaries
print("dictionaries:")
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

phonebook = {
    "John" : 938477566,
    "jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

#Iterating over dictionaries
print("Iterating over dictionaries:")
phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))
    
# Removing a value
print("Removing a value:")
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
del phonebook["Jack"]
print(phonebook)

phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
phonebook.pop("John")
print(phonebook)

phonebook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}  

# example
print("example:")
phonebook["Jake"] = 938273443  
del phonebook["Jill"]  
if "Jake" in phonebook:  
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:      
    print("Jill is not listed in the phonebook.")  
