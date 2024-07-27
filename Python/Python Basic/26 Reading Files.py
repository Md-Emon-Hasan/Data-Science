# check readable or not
# "r" use for file read and readable or not
employee_file = open("employees.txt", "r")
print(employee_file.readable())
employee_file.close()

# file read
employee_file = open("employees.txt", "r")
print(employee_file.read())
employee_file.close()

# reading first line
employee_file = open("employees.txt", "r")
print(employee_file.readline())
employee_file.close()

# reading first line with index value
employee_file = open("employees.txt", "r")
print(employee_file.readlines())
employee_file.close

employee_file = open("employees.txt", "r")
for emon in employee_file.readlines():
    print(emon)
employee_file.close

