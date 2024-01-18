from new_student import Student

student = Student(name="Edward", surname="agle")
print(student)
try:
    student2 = Student(name="Edward", surname="agle", id="toto")
    print(student)
except Exception as e:
    print(e)
