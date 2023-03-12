students = {}

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = int(input("Enter student grade: "))
    students[name] = {"age": age, "grade": grade}

def remove_student():
    name = input("Enter student name: ")
    if name in students:
        del students[name]
        print(f"{name} has been removed.")
    else:
        print(f"{name} is not in the system.")

def display_students():
    print("Student Information:")
    print("--------------------")
    for name, info in students.items():
        print(f"{name}: Age - {info['age']}, Grade - {info['grade']}")
        
def menu():
    while True:
        print("""
        1. Add Student
        2. Remove Student
        3. Display Students
        4. Exit
        """)
        choice = input("Enter choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            display_students()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

menu()