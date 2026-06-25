student = {"name":"unni",
           "age":25,
           "course":"python"}

print(student)

student["name"] = "unnikuttan"
print(student)

student.pop("age")
print(student)
student.popitem()
print(student)
student.clear()
print(student)
del(student)
print(student)