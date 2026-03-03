class Course:
    def __init__(self, course_title, course_code, award, nfq_level):
        self.course_title = course_title
        self.course_code = course_code
        self.award = award
        self.nfq_level = nfq_level
        self.__students = []  

    def get_course_title(self):
        return self.course_title
    
    def get_course_code(self):
        return self.course_code
    
    def get_award(self):
        return self.award
    
    def get_nfq_level(self):
        return self.nfq_level
    
    def get_students(self):
        return self.__students

    def set_course_title(self, course_title):
        self.course_title = course_title
    
    def set_course_code(self, course_code):
        self.course_code = course_code
    
    def set_award(self, award):
        self.award = award
    
    def set_nfq_level(self, nfq_level):
        self.nfq_level = nfq_level
    
    def add_student(self, student):
        self.__students.append(student)

    def display_all_students(self):
        print(f"\nStudents in {self.course_title}:")
        for student in self.__students:
            print(student)