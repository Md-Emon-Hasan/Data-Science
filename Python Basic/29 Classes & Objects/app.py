# create an object
from Student import Student

student1 = Student("Jim", "Business", 3.5, False)
student2 = Student("Harry", "Teacher", 3.6, True)

print(student1.gpa)
print(student2.name)
print(student2.is_on_probation)