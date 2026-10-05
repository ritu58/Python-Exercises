students = []


def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    department = input("Enter department: ")

    student = {
        "name": name,
        "age": age,
        "department": department
    }

    students.append(student)

    print("Student added successfully!\n")



def view_students():

    if len(students) == 0:
        print("No students available\n")

    else:
        print("\nStudent List:")

        for i, student in enumerate(students):

            print("Student No:", i+1)
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Department:", student["department"])
            print("------------------")



def search_student():

    name = input("Enter student name to search: ")

    for student in students:

        if student["name"] == name:

            print("Student Found")
            print(student)
            return

    print("Student not found")



while True:

    print("\n===== Student Management System =====")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")


    choice = input("Enter choice: ")


    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        print("Program Closed")
        break

    else:
        print("Invalid choice")