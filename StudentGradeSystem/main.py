import student_info
import grades
import awards

def get_yes_no(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Invalid response! Please enter yes or no.")

def main():
    print("===== STUDENT GRADE SYSTEM =====\n")
    
    while True:
        name, student_id, course, year_level, section = student_info.get_student_info()
        grade_list, average = grades.get_grades_and_average()
        award = awards.determine_award(average)
        
        print(f"\nName: {name}")
        print(f"Student ID: {student_id}")
        print(f"Course: {course}")
        print(f"Year Level: {year_level}")
        print(f"Section: {section}")
        
        print("\n\n===== GRADES =====\n")
        for i, grade in enumerate(grade_list, 1):
            formatted_grade = int(grade) if grade.is_integer() else grade
            print(f"Subject {i}: {formatted_grade}")
            
        print(f"\nAverage: {average:.2f}")
        print(f"Award: {award}\n")
        
        if not get_yes_no("Do you want to enter another student? (yes/no): "):
            break
        print("\n" + "=" * 30 + "\n")

if __name__ == "__main__":
    main()