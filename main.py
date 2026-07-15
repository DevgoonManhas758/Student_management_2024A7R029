from student import Student


students = []


def add_student():

    roll = int(input("Enter Roll Number: "))

    for student in students:
        if student.roll_no == roll:
            print("Roll Number already exists")
            return

    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))

    if not Student.validate_marks(marks):
        print("Invalid Marks")
        return

    student = Student(roll, name, marks)

    students.append(student)

    print("Student Added Successfully")


def view_students():

    if not students:
        print("No Students Found")
        return

    for student in students:
        student.display()



def search_student():

    roll = int(input("Enter Roll Number: "))

    for student in students:
        if student.roll_no == roll:
            student.display()
            return

    print("Student Not Found")



def update_marks():

    roll = int(input("Enter Roll Number: "))

    for student in students:

        if student.roll_no == roll:

            marks = int(input("Enter New Marks: "))

            if Student.validate_marks(marks):
                student.marks = marks
                print("Marks Updated Successfully")
            else:
                print("Invalid Marks")

            return

    print("Student Not Found")



def delete_student():

    roll = int(input("Enter Roll Number: "))

    for student in students:

        if student.roll_no == roll:
            students.remove(student)
            print("Student Deleted Successfully")
            return

    print("Student Not Found")



def show_topper():

    if not students:
        print("No Students Found")
        return

    topper = students[0]

    for student in students:
        if student.marks > topper.marks:
            topper = student

    print("Topper Student:")
    topper.display()



def menu():

    while True:

        print("""
==============================
 Student Management System
==============================

1. Add Student
2. View Students
3. Search Student
4. Update Marks
5. Delete Student
6. Show Topper
7. Exit
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_marks()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            show_topper()

        elif choice == "7":
            print("Thank you!")
            break

        else:
            print("Invalid Choice")



if __name__ == "__main__":
    menu()