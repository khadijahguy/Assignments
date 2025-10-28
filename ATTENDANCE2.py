# Creator : Khady Gueye

""" This is the Attendance program. """

# Person class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Education class
class Education:
    def __init__(self, school, major):
        self.school = school
        self.major = major

# Course class
class Course(Education):
    def __init__(self, school, major, course_name):
        super().__init__(school, major)  
        self.course_name = course_name

# Student class 
class Student(Person, Course):
    def __init__(self, name, age, school, major, course_name):
        Person.__init__(self, name, age) 
        Course.__init__(self, school, major, course_name)

    def print_student_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"School: {self.school}")
        print(f"Major: {self.major}")
        print(f"Course: {self.course_name}")

# Example 
student1 = Student("Alice", 20, "Harvard University", "Computer Science", "Introduction to Programming")
student1.print_student_info()
