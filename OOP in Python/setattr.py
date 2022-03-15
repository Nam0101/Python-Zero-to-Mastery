class Student:
  marks = 88
  name = 'Sheeran'

person = Student()

# set value of name to Adam
setattr(person, 'name', 'Adam')
print(person.name)

# set value of marks to 78
setattr(person, 'marks', 78)
print(person.marks)

# Output: Adam
#         78