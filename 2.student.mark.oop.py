class Student:
    def __init__(self, sid, name, dob):
        self.__id = sid
        self.__name = name
        self.__dob = dob

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name
    def display(self):
        return f"Student ID: {self.__id}, Name: {self.__name}, DoB: {self.__dob}"

class Course:
    """
    Class đại diện cho Khóa học.
    """
    def __init__(self, cid, name):
        self.__id = cid
        self.__name = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def display(self):
        return f"Course ID: {self.__id}, Name: {self.__name}"

class SchoolSystem:
    """
    Class quản lý chính, chứa danh sách sinh viên, môn học và điểm.
    """
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def input_students(self):
        num = int(input("Enter number of students: "))
        for _ in range(num):
            sid = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            dob = input("Enter Date of Birth (DD/MM/YYYY): ")
            student = Student(sid, name, dob)
            self.students.append(student)

    def input_courses(self):
        num = int(input("Enter number of courses: "))
        for _ in range(num):
            cid = input("Enter Course ID: ")
            name = input("Enter Course Name: ")
            course = Course(cid, name)
            self.courses.append(course)

    def list_students(self):
        print("\n--- Student List ---")
        for s in self.students:
            print(s.display())

    def list_courses(self):
        print("\n--- Course List ---")
        for c in self.courses:
            print(c.display())

    def input_marks(self):
        print("\n--- Input Marks ---")
        self.list_courses()
        course_id = input("Select Course ID to input marks: ")
        
        if not any(c.get_id() == course_id for c in self.courses):
            print("Course not found!")
            return

        for s in self.students:
            mark = float(input(f"Enter mark for {s.get_name()} (ID: {s.get_id()}): "))
            data = {
                "course_id": course_id,
                "student_id": s.get_id(),
                "mark": mark
            }
            self.marks.append(data)

    def show_student_marks(self):
        print("\n--- Show Marks ---")
        self.list_courses()
        course_id = input("Enter Course ID to view marks: ")
        
        print(f"\nMarks for Course {course_id}:")
        for m in self.marks:
            if m['course_id'] == course_id:
                student_name = "Unknown"
                for s in self.students:
                    if s.get_id() == m['student_id']:
                        student_name = s.get_name()
                        break
                print(f"Student: {student_name} (ID: {m['student_id']}) - Mark: {m['mark']}")

if __name__ == "__main__":
    system = SchoolSystem()
    system.input_students()
    system.input_courses()

    while True:
        print("\n=======================")
        print("MENU:")
        print("1. List Students")
        print("2. List Courses")
        print("3. Input Marks")
        print("4. Show Marks")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            system.list_students()
        elif choice == '2':
            system.list_courses()
        elif choice == '3':
            system.input_marks()
        elif choice == '4':
            system.show_student_marks()
        elif choice == '5':
            break
        else:
            print("Invalid choice!")