class Student:
    def _init_(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age

    def _str_(self):
        return f"ID: {self.student_id} - Name: {self.name} - Age: {self.age}"


class StudentRegistry:
    def _init_(self):
        self.students = []

    def add_student(self, student):
        for s in self.students:
            if s.student_id == student.student_id:
                print("Student with this ID already exists.")
                return
        self.students.append(student)
        print("Student added successfully.")

    def remove_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                self.students.remove(s)
                print("Student removed successfully.")
                return
        print("Student not found.")

    def find_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                print(s)
                return
        print("Student not found.")

    def list_students(self):
        if not self.students:
            print("No students registered.")
        else:
            for s in self.students:
                print(s)
