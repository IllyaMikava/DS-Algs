class Student:
    def __init__(self, fname,lname,id,year,email,pps,middleName):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.year = year
        self.email = email
        self.__pps = pps  # Private attribute
        self.__middleName = middleName  # Private attribute

     # Getters
    def get_fname(self):
        return self.fname
    
    def get_lname(self):
        return self.lname
    
    def get_id(self):
        return self.id
    
    def get_email(self):
        return self.email
    
    # Setters
    def set_fname(self, fname):
        self.fname = fname
    
    def set_lname(self, lname):
        self.lname = lname
    
    def set_id(self, id):
        self.id = id
    
    def set_email(self, email):
        self.email = email
    
    def __str__(self):
        return f"{self.fname} {self.lname} - {self.id} - {self.email}"
