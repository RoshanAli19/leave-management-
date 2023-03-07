class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.leaves = 5  # Each student gets 5 leaves by default

    def request_leave(self, days):
        if days <= self.leaves:
            self.leaves -= days
            print(f"{self.name} has been granted leave for {days} days.")
        else:
            print(f"{self.name} does not have enough leaves.")

    def check_leaves(self):
        print(f"{self.name} has {self.leaves} leaves left.")


class Faculty:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
        self.leaves = 20  # Each faculty member gets 20 leaves by default

    def request_leave(self, days):
        if days <= self.leaves:
            self.leaves -= days
            print(f"{self.name} has been granted leave for {days} days.")
        else:
            print(f"{self.name} does not have enough leaves.")

    def check_leaves(self):
        print(f"{self.name} has {self.leaves} leaves left.")


class LeaveManagement:
    def __init__(self):
        self.students = []
        self.faculty = []

    def add_student(self, name, roll_no):
        self.students.append(Student(name, roll_no))

    def add_faculty(self, name, emp_id):
        self.faculty.append(Faculty(name, emp_id))

    def grant_leave(self, person_type, name, days):
        if person_type == "student":
            for student in self.students:
                if student.name == name:
                    student.request_leave(days)
                    return
            print("Student not found.")
        elif person_type == "faculty":
            for faculty in self.faculty:
                if faculty.name == name:
                    faculty.request_leave(days)
                    return
            print("Faculty member not found.")
        else:
            print("Invalid person type.")

    def check_leaves(self, person_type, name):
        if person_type == "student":
            for student in self.students:
                if student.name == name:
                    student.check_leaves()
                    return
            print("Student not found.")
        elif person_type == "faculty":
            for faculty in self.faculty:
                if faculty.name == name:
                    faculty.check_leaves()
                    return
            print("Faculty member not found.")
        else:
            print("Invalid person type.")


# Example usage:

lm = LeaveManagement()

lm.add_student("John", "1234")
lm.add_faculty("Jane", "5678")

lm.grant_leave("student", "John", 2)  # John is granted leave for 2 days
lm.grant_leave("faculty", "Jane", 15)  # Jane is granted leave for 15 days

lm.check_leaves("student", "John")  # Prints "John has 3 leaves left."
lm.check_leaves("faculty", "Jane")  # Prints "Jane has 5 leaves left."
