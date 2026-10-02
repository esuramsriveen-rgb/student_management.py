import json


class Student:

    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def to_dict(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "grade": self.grade
        }


class Manager:

    def __init__(self):
        self.students = []
        self.filename = "students.json"
        self.load_students()

    def load_students(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)

            for item in data:
                student = Student(
                    item["id"],
                    item["name"],
                    item["grade"]
                )
                self.students.append(student)

        except FileNotFoundError:
            self.students = []

        except json.JSONDecodeError:
            print("Invalid JSON file. Starting with empty records.")
            self.students = []

    def save_students(self):
        data = []

        for student in self.students:
            data.append(student.to_dict())

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def add_student(self, student):
        for existing_student in self.students:
            if existing_student.student_id == student.student_id:
                print("Error: Student ID already exists.")
                return

        self.students.append(student)
        self.save_students()
        print("Student added successfully.")

    def list_students(self):
        if not self.students:
            print("No students found.")
            return

        print("\n===== Student List =====")

        for student in self.students:
            print("ID:", student.student_id)
            print("Name:", student.name)
            print("Grade:", student.grade)
            print("--------------------")

    def update_student(self, student_id, name, grade):
        for student in self.students:
            if student.student_id == student_id:
                student.name = name
                student.grade = grade
                self.save_students()
                print("Student updated successfully.")
                return

        print("Student ID not found.")

    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                self.save_students()
                print("Student deleted successfully.")
                return

        print("Student ID not found.")


def get_student_id():
    while True:
        try:
            student_id = int(input("Enter Student ID: "))

            if student_id <= 0:
                print("ID must be a positive number.")
            else:
                return student_id

        except ValueError:
            print("Please enter a valid number.")


def main():
    manager = Manager()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. List Students")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = get_student_id()

            name = input("Enter Student Name: ").strip()

            if name == "":
                print("Name cannot be empty.")
                continue

            grade = input("Enter Grade: ").strip()

            if grade == "":
                print("Grade cannot be empty.")
                continue

            student = Student(student_id, name, grade)
            manager.add_student(student)

        elif choice == "2":
            student_id = get_student_id()

            name = input("Enter New Name: ").strip()

            if name == "":
                print("Name cannot be empty.")
                continue

            grade = input("Enter New Grade: ").strip()

            if grade == "":
                print("Grade cannot be empty.")
                continue

            manager.update_student(student_id, name, grade)

        elif choice == "3":
            student_id = get_student_id()
            manager.delete_student(student_id)

        elif choice == "4":
            manager.list_students()

        elif choice == "5":
            print("Thank you for using Student Management System!")
            break

        else:
            print("Invalid choice. Please select 1 to 5.")


main()