students = []
courses = []
marks = []


def input_number_of_students():
    """Nhập số lượng sinh viên"""
    count = int(input("Enter number of students: "))
    return count

def input_student_info():
    """Nhập thông tin sinh viên: id, name, DoB"""
    print("\n--- Input Student Information ---")
    sid = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    dob = input("Enter Date of Birth (DD/MM/YYYY): ")
    student = {
        "id": sid,
        "name": name,
        "dob": dob
    }
    students.append(student)

def input_number_of_courses():
    """Nhập số lượng môn học"""
    count = int(input("\nEnter number of courses: "))
    return count

def input_course_info():
    """Nhập thông tin môn học: id, name"""
    print("\n--- Input Course Information ---")
    cid = input("Enter Course ID: ")
    name = input("Enter Course Name: ")
    
    course = {
        "id": cid,
        "name": name
    }
    courses.append(course)

def input_marks():
    """Chọn môn học và nhập điểm cho sinh viên"""
    print("\n--- Input Marks ---")
    list_courses()
    course_id = input("Select Course ID to input marks: ")
    
    if not any(c['id'] == course_id for c in courses):
        print("Course not found!")
        return

    print(f"Inputting marks for course: {course_id}")
    for s in students:
        mark = float(input(f"Enter mark for student {s['name']} (ID: {s['id']}): "))
        data = {
            "course_id": course_id,
            "student_id": s['id'],
            "mark": mark
        }
        marks.append(data) # 

def list_students():
    """Hiển thị danh sách sinh viên"""
    print("\n--- Student List ---")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, DoB: {s['dob']}")

def list_courses():
    """Hiển thị danh sách môn học"""
    print("\n--- Course List ---")
    for c in courses:
        print(f"ID: {c['id']}, Name: {c['name']}") 

def show_student_marks():
    """Hiển thị bảng điểm cho một môn học cụ thể"""
    print("\n--- Show Marks ---")
    list_courses()
    course_id = input("Enter Course ID to view marks: ")
    
    print(f"\nMarks for Course {course_id}:")
    found = False
    for m in marks:
        if m['course_id'] == course_id:
            s_name = next((s['name'] for s in students if s['id'] == m['student_id']), "Unknown")
            print(f"Student: {s_name} (ID: {m['student_id']}) - Mark: {m['mark']}")
            found = True
    
    if not found:
        print("No marks found for this course.")


if __name__ == "__main__":
    try:
        num_students = input_number_of_students()
        for _ in range(num_students):
            input_student_info()

        num_courses = input_number_of_courses()
        for _ in range(num_courses):
            input_course_info()
        
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
                list_students()
            elif choice == '2':
                list_courses()
            elif choice == '3':
                input_marks()
            elif choice == '4':
                show_student_marks()
            elif choice == '5':
                break
            else:
                print("Invalid choice!")
                
    except ValueError:
        print("Please enter valid numbers.")