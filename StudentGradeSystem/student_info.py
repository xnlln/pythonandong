def get_student_info():
    print("===== STUDENT INFORMATION =====\n")
    name = input("Name: ").strip()
    student_id = input("Student ID: ").strip()
    course = input("Course: ").strip()
    year_level = input("Year Level: ").strip()
    section = input("Section: ").strip()
    return name, student_id, course, year_level, section