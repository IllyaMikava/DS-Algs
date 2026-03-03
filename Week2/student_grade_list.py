from grade_list import GradeList

class StudentGradeList(GradeList):
    def __init__(self):
        self.__students = []
    
    def add_student(self, name, email, grade):
        self.__students.append((name, email, grade))

    def search(self, email):
        for student in self.__students:
            if student[1] == email:
                return student
        return None
    
    def delete_student(self, email):
        for i in range(len(self.__students)):
            if self.__students[i][1] == email:
                del self.__students[i]
                return True
        return False
    
    def highest_grade(self):
        if not self.__students:
            return []
        
        highest_grade = self.__students[0][2]
        for student in self.__students:
            if student[2] > highest_grade:
                highest_grade = student[2]
        
        top_students = []
        for student in self.__students:
            if student[2]== highest_grade:
                top_students.append(student)
        
        return top_students
    
    def size(self):
        return len(self.__students)

        