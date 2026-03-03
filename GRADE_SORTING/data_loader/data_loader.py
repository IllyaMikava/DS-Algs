import csv
from models.student import Student

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.__stundent_grades = []
        self.load_data()
    
    def load_data(self):
        with open(self.file_path, newline = '', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                student = Student(
                    student_name = row['Student Name'],
                    course = row ['Course'],
                    module = row['Module'],
                    grade = row['Grade (%)']    
                )
                self.__stundent_grades.append(student)
    
    def get_all_data(self):
        return self.__stundent_grades.copy()
    
    def  get_data_by_size(self, size):
        if size < 0:
            raise ValueError("Size must not be negative")

        return self.__stundent_grades[:size]
    
    def get_by_module(self, module_name):
        results = []

        for student in self.__stundent_grades:
            if student.module == module_name:
                results.append(student)
        return results