from student_registry import Student, StudentRegistry

def main():
    registry = StudentRegistry()

    while True:
        print("\nStudent Registry")
        print("1. Add student")
        print("2. Remove student")
        print("3. Find student")
        print("4. List students")
        print("5. Exit")

        option = input("Choose an option (1-5): ")

        if option == "1":
            student_id = input("Student ID: ")
            name = input("Name: ")
            age = input("Age: ")
            student = Student(student_id, name, age)
            registry.add_student(student)

        elif option == "2":
            student_id = input("Student ID to remove: ")
            registry.remove_student(student_id)

        elif option == "3":
            student_id = input("Student ID to find: ")
            registry.find_student(student_id)

        elif option == "4":
            registry.list_students()

        elif option == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1 and 5.")


if _name_ == "_main_":
    main()
