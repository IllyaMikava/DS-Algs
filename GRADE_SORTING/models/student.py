class Student:
    def __init__(self, student_name, course, module, grade):
        self.student_name = student_name
        self.course = course
        self.module = module
        self.grade = float(grade) # Convert to float for numeric operations

    def __repr__(self):
        return f"Student({self.student_name}, {self.course}, {self.module}, {self.grade}%)"