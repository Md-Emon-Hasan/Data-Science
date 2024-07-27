# Syntax
# f = open("harry.txt", "rt")
# f = open("demofile.txt", "rt")

# f = open('harry.txt','r')
# content = f.read()
# print(content)

# Return the 5 first characters of the file
# f = open('harry.txt','r')
# print(f.read(5))

# read one line the file
# f = open('harry.txt','r')
# print(f.readline())
# print(f.readline())

# Loop through the file line by line:
# f = open('harry.txt','r')
# for x in f:
#    print(x)
    
# Close the file when you are finish with it:
# f = open('harry.txt','r')
# print(f.readline())
# f.close()

# Open the file and append content to the file:
# f = open('harry.txt','a')
# f.write('now the file has more content!')
# f.close()
# f = open('harry.txt','r')
# print(f.read())

# Open the file and overwrite the content:
# f = open('harry.txt','w')
# f.write('woops! i have deleted the content!')
# f.close()
# f = open('harry.txt','r')
# print(f.read())

# Create a new file if it does not exist:
f = open('harry1.txt','w')

# Remove the file "demofile.txt":
# import os
# os.remove('harry1.txt')

# Check if File exist:
# import os
# if os.path.exists('harry1.txt'):
#     os.remove('harry1.txt')
# else:
#     print('the file does not exist')
    
# Remove the folder "myfolder":
# import os
# os.rmdir('myfolder')
