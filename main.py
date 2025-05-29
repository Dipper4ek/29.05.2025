import sqlite3
from tabulate import tabulate

connection = sqlite3.connect('Students_db.db')
cursor = connection.cursor()

while True:
    print("Menu:")
    print("1: Show all students")
    print("2: Show all courses")
    print("3: Show students and their courses")
    print("4: Register student to course")
    print("5: Register student to students")
    print("x: Exit\n")

    choice = input("Your choice: ")

    if choice == "1":
        cursor.execute("SELECT * FROM students")
        data = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]
        print("\nAll students:")
        print(tabulate(data, headers=column_names, tablefmt="pretty"))
        print()

    elif choice == "2":
        cursor.execute("SELECT * FROM courses")
        data = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]
        print("\nAll courses:")
        print(tabulate(data, headers=column_names, tablefmt="pretty"))
        print()

    elif choice == "3":
        query = """
                SELECT students.name AS Student, courses.course_name AS Course
                FROM students_on_courses
                JOIN students ON students_on_courses.student_id = students.id
                JOIN courses ON students_on_courses.course_id = courses.course_id
                """
        cursor.execute(query)
        data = cursor.fetchall()
        print("\nStudents and their courses:")
        print(tabulate(data, headers=["Student", "Course"], tablefmt="pretty"))
        print()


    elif choice == "4":
        print("\nRegister student to a course:")
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")

        try:
            cursor.execute("INSERT INTO students_on_courses (student_id, course_id) VALUES (?, ?)",
                           (student_id, course_id))
            connection.commit()
            print("Student was registered to the course.\n")
        except sqlite3.Error as e:
            print("Error:", e, "\n")


    elif choice == "5":
        print("\nRegister student:")
        student_id = input("Enter student ID: ")
        student_name = input("Enter student Name: ")
        student_age = input("Enter student Age: ")
        student_major = input("Enter sudent Major: ")

        try:
            cursor.execute("INSERT INTO students (id, name, age, major) VALUES (?, ?, ?, ?)",
                            (student_id, student_name, student_age, student_major))
            connection.commit()
            print("Student was registered to the Students.\n")
        except sqlite3.Error as e:
            print("Error", e, "\n")





    elif choice == "x":
        print("Goodbye!")
        connection.close()
        break

    else:
        print("Wrong option. Try again.\n")
