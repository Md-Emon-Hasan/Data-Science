# for loops
list = ['harry', 'larry', 'carry', 'marie']
for item in list:
    print(item)
    
list = [['harry', 1], ['larry', 2], ['carry', 6], ['marie', 250]]
for item, lollypop in list:
    print(item, lollypop)
    
list = [['harry', 1], ['larry', 2], ['carry', 6], ['marie', 250]]
dict1 = dict(list)
print(dict1)
for item, lollypop in list:
    print(item, 'and lolly is', lollypop)
    
list = [['harry', 1], ['larry', 2], ['carry', 6], ['marie', 250]]
dict1 = dict(list)
for item in dict1:
    print(item)
    
items = [int, float, 'harry', 5,3,3,22,21,64,23,233,23]
for item in items:
    if str(item).isnumeric() and item>6:
        print(item)
    
