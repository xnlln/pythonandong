def get_grades_and_average():
    print("\n===== GRADES =====\n")
    grades = []
    for i in range(1, 9):
        while True:
            try:
                grade = float(input(f"Subject {i}: "))
                if grade < 0 or grade > 100:
                    print("Invalid grade! Please enter a value between 0 and 100.")
                else:
                    grades.append(grade)
                    break
            except ValueError:
                print("Invalid input! Please enter a numerical value.")
                
    average = sum(grades) / len(grades)
    return grades, average