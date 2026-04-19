class Student:
    def __init__(self, name, grade, student_id):
        self.name = name
        self.grade = grade
        self.student_id = student_id

    def __repr__(self):
        return f"Student(name={self.name}, grade={self.grade}, student_id={self.student_id})"