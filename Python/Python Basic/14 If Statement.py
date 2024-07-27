from operator import truediv

# if statement
is_male = True
if is_male:
    print("You are a male")
    
is_male = False
if is_male:
    print("You are a male")
else:
    print("Tou are not a male")

is_male = True
is_tall = False
if is_male or is_tall:
    print("You are male or tall or both")
else:
    print("You are neither male or tall")
    
is_male = True
is_tall = False
if is_male and is_tall:
    print("You are a male and tall")
elif is_male and not is_tall:
    print("You are a male but not a tall")
elif not is_male and is_tall:
    print("You are not a male but tall")
else:
    print("You are neither male or tall")
