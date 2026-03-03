class GradeList:
    def add_student(self, name, email, grade):
        raise NotImplementedError("add_student() msut be implemented")
    
    def search(self, email):
        raise NotImplementedError("search() msut be implemented")
    
    def delete_student(self, email):
        raise NotImplementedError("delete_student() msut be implemented")
    
    def highest_grade(self):
        raise NotImplementedError("highest_grade() msut be implemented")
    
    def size(self):
        raise NotImplementedError("size() msut be implemented")