# Creator : Khady Gueye

""" This is a simple gradebook program. """

# Exception class for whem roster is empty
class EmptyRosterError(Exception):
    pass

# Exception class for when a student is not found
class StudentNotFoundError(Exception):
    pass

# Exception cladd for when a grade item is not found
class GradeItemNotFoundError(Exception):
    pass

# A class to hold students information
class Student:
    def __init__(self, first_name, last_name, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
    
    def get_student_id(self):
        return self.student_id
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name

# A class to hold assignment information
class GradeItem:
    def __init__(self, name, total_points):
        self.name = name
        self.total_points = total_points
        self.grades = {}  # Dictionary of student grades
    
    def get_name(self):
        return self.name
    
    def get_total_points(self):
        return self.total_points
    
    def add_student_grade(self, student_id, grade):
        self.grades[student_id] = grade
    
    def get_student_grade(self, student_id):
        return self.grades.get(student_id, None)

# A class to hold course information
class Course:
    def __init__(self):
        self.roster = []
        self.grade_items = [] 

    # Add student
    def add_student(self, student):
        self.roster.append(student)
    
    # Add students assignments
    def add_grade_item(self, grade_item):
        self.grade_items.append(grade_item)
    
    # Add students grades
    def add_student_grade(self, grade_item_name, student_id, grade):
        # Check if roster is empty
        if not self.roster:
            raise EmptyRosterError("Exception: Course Roster is Empty.")
        
        # Find student
        student_found = False
        for student in self.roster:
            if student.get_student_id() == student_id:
                student_found = True
                break
        if not student_found:
            raise StudentNotFoundError(f"Exception: Student ({student_id} not found.")
        
        # Find grade item
        grade_item_found = False
        for grade_item in self.grade_items:
            if grade_item.get_name() == grade_item_name:
                grade_item_found = True
                grade_item.add_student_grade(student_id, grade)
                break
        if not grade_item_found:
            raise GradeItemNotFoundError(f"Exception: Grade Item ({grade_item_name}) not found.")
    
    # Print students grades
    def print_student_grades(self, student_id):
        if not self.roster:
            raise EmptyRosterError("Exception: Course Roster is Empty.")
        
        student_found = False
        for student in self.roster:
            if student.get_student_id() == student_id:
                student_found = True
                grades_line = f"{student.get_first_name()} {student.get_last_name()} ({student_id})"
                for grade_item in self.grade_items:
                    grade = grade_item.get_student_grade(student_id)
                    total_points = grade_item.get_total_points()
                    grades_line += f" | {grade_item.get_name()}: {grade if grade is not None else 'N/A'} ({total_points})"
                print(grades_line)
                break
        if not student_found:
            raise StudentNotFoundError(f"Exception: Student ({student_id}) not found.")

    # Print class roster
    def print_roster(self):
        if not self.roster:
            raise EmptyRosterError("Exception: Course Roster is Empty.")
        
        print("\n \nCourse Roster:")
        for student in self.roster:
            print(f"{student.get_last_name()}, {student.get_first_name()} ({student.get_student_id()})")
    
    # Print the overall class grades (everyone)
    def print_class_grades(self):
        if not self.roster:
            raise EmptyRosterError("Exception: Course Roster is Empty.")
        
        print("Class Grades:")
        for student in self.roster:
            grades_line = f"{student.get_first_name()} {student.get_last_name()} ({student.get_student_id()})"
            for grade_item in self.grade_items:
                grade = grade_item.get_student_grade(student.get_student_id())
                total_points = grade_item.get_total_points()
                grades_line += f" | {grade_item.get_name()}: {grade if grade is not None else 'N/A'} ({total_points})"
            print(grades_line)

# Define Main Function
def main():
    course = Course()
    # Print Welcome Menu
    print("\nWelcome to CSC/DSCI 1301: Principle in CS/DS 1 \nPlease choose one of the following options (Enetr 'quit' or 'q' to exit).")
    print("1. Add a Student.")
    print("2. Add a Grade Item.")
    print("3. Add a Student's Grades.")
    print("4. Print Student's Grades.")
    print("5. Print Course Roster.")
    print("6. Print Class Grades.")
    
    while True:
        choice = input("\n:> ").lower()
        
        try:
            # Check for quit
            if choice == 'quit' or choice == 'q':
                break
            else :
                # Check for Number choice
                if choice == '1':
                    first_name = input("Enter First Name: ")
                    last_name = input("Enter Last Name: ")
                    student_id = int(input("Enter Student ID: "))
                    student = Student(first_name, last_name, student_id)
                    course.add_student(student)
                elif choice == '2':
                    name = input("Enter grade item name: ")
                    total_points = int(input("Enter the total points for grade item: "))
                    grade_item = GradeItem(name, total_points)
                    course.add_grade_item(grade_item)
                elif choice == '3':
                    grade_item_name = input("Enter grade item name: ")
                    student_id = int(input("Enter Student ID: "))
                    grade = int(input("\nEnter Student Grade: "))
                    course.add_student_grade(grade_item_name, student_id, grade)
                elif choice == '4':
                    student_id = int(input("Enter Student ID: "))
                    print(' ')
                    course.print_student_grades(student_id)
                elif choice == '5':
                    course.print_roster()
                elif choice == '6':
                    course.print_class_grades()
                else:
                    print("Wrong choice. Please try again.")
        except ValueError:
            print("Error: Enter a Integer Student ID")
        except EmptyRosterError as e:
            print(e)
        except StudentNotFoundError as e:
            print(e)
        except GradeItemNotFoundError as e:
            print(e)

# Call main function
if __name__ == "__main__":
    main()
