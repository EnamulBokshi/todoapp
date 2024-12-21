# from customtkinter import*
import openpyxl
from openpyxl import Workbook
# Define the Course class
class Course:
    def _init_(self, course_id, course_name, instructor):
        self.course_id = course_id
        self.course_name = course_name
        self.instructor = instructor
        self.contents = []  # List to store Content objects
        self.students = []  # List to store Student objects

    def add_content(self, content):
        self.contents.append(content)
        print(f"Content '{content.title}' added to course '{self.course_name}'.")


    def enroll_student(self, student):
        self.students.append(student)
        print(f"Student '{student.name}' enrolled in course '{self.course_name}'.")

    def view_details(self):
        print(f"\nCourse ID: {self.course_id}")
        print(f"Course Name: {self.course_name}")
        print(f"Instructor: {self.instructor}")
        print("Contents:")
        for content in self.contents:
            print(f"- {content.content_id}: {content.title}")
        print("Students:")
        for student in self.students:
            print(f"- {student.student_id}: {student.name}")


# Define the Content class
class Content:
    def _init_(self, content_id, title, description, link):
        self.content_id = content_id
        self.title = title
        self.description = description
        self.link = link


# Define the Student class
class Student:
    def _init_(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.enrolled_courses = []  # List of Course objects

    def enroll(self, course):
        self.enrolled_courses.append(course)
        print(f"Enrolled in course: {course.course_name}")


# Define the CMS class
class CMS:
    def _init_(self):
        self.courses = []
        self.students = []

    def load_courses(self):
        try:
            workbook = openpyxl.load_workbook("courses.xlsx")
            sheet = workbook.active
            for row in sheet.iter_rows(min_row=2, values_only=True):
                course = Course(row[0], row[1], row[2])
                self.courses.append(course)
            print("Courses loaded successfully.")
        except FileNotFoundError:
            print("No existing course data found. Creating new file...")
            self.save_courses()

    def load_students(self):
        try:
            workbook = openpyxl.load_workbook("students.xlsx")
            sheet = workbook.active
            for row in sheet.iter_rows(min_row=2, values_only=True):
                student = Student(row[0], row[1])
                self.students.append(student)
            print("Students loaded successfully.")
        except FileNotFoundError:
            print("No existing student data found. Creating new file...")
            self.save_students()

    def save_courses(self):
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Courses"
        sheet.append(["Course ID", "Course Name", "Instructor"])  # Add headers
        for course in self.courses:
            sheet.append([course.course_id, course.course_name, course.instructor])
        workbook.save("courses.xlsx")
        print("Courses saved successfully.")

    def save_students(self):
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Students"
        sheet.append(["Student ID", "Name"])  # Add headers
        for student in self.students:
            sheet.append([student.student_id, student.name])
        workbook.save("students.xlsx")
        print("Students saved successfully.")

    def instructor_menu(self):
        while True:
            print("\nInstructor Menu:")
            print("1. Create Course")
            print("2. Add Content to Course")
            print("3. View Course Details")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                course_id = input("Enter Course ID: ")
                course_name = input("Enter Course Name: ")
                instructor = input("Enter Instructor Name: ")
                course = Course(course_id, course_name, instructor)
                self.courses.append(course)
                self.save_courses()  # Save courses immediately
                print(f"Course '{course_name}' created successfully!")
            elif choice == '2':
                course_id = input("Enter Course ID: ")
                course = next((c for c in self.courses if c.course_id == course_id), None)
                if course:
                    content_id = input("Enter Content ID: ")
                    title = input("Enter Content Title: ")
                    description = input("Enter Description: ")
                    link = input("Enter Content Link: ")
                    content = Content(content_id, title, description, link)
                    course.add_content(content)
                else:
                    print("Course not found!")
            elif choice == '3':
                course_id = input("Enter Course ID: ")
                course = next((c for c in self.courses if c.course_id == course_id), None)
                if course:
                    course.view_details()
                else:
                    print("Course not found!")
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def student_menu(self):
        while True:
            print("\nStudent Menu:")
            print("1. Enroll in Course")
            print("2. View Enrolled Courses")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                student_id = input("Enter Student ID: ")
                student_name = input("Enter Student Name: ")
                student = next((s for s in self.students if s.student_id == student_id), None)
                if not student:
                    student = Student(student_id, student_name)
                    self.students.append(student)

                course_id = input("Enter Course ID to enroll: ")
                course = next((c for c in self.courses if c.course_id == course_id), None)
                if course:
                    student.enroll(course)
                    course.enroll_student(student)
                    self.save_students()  # Save students immediately
                else:
                    print("Course not found!")
            elif choice == '2':
                student_id = input("Enter Student ID: ")
                student = next((s for s in self.students if s.student_id == student_id), None)
                if student:
                    print("\nEnrolled Courses:")
                    for course in student.enrolled_courses:
                        print(f"- {course.course_id}: {course.course_name}")
                else:
                    print("Student not found!")
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")

    def run(self):
        self.load_courses()
        self.load_students()
        while True:
            print("\nWelcome to the Course Content Management System!")
            print("1. Instructor Login")
            print("2. Student Login")
            print("3. Exit")
            role = input("Choose your role: ")

            if role == '1':
                self.instructor_menu()
            elif role == '2':
                self.student_menu()
            elif role == '3':
                self.save_courses()
                self.save_students()
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


# Run the CMS
cms = CMS()
cms.run()