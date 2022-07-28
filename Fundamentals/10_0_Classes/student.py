class Student:
    class_name = "Student"

    def __init__(self):
        self.name = "Test"
        self.age = 0


# calling class variable
print(Student.class_name)

# creating instance
student_inst = Student()

# calling instance fields
print(student_inst.name)
print(student_inst.age)

# setting instance field and print
student_inst.age = 20
print(student_inst.age)
