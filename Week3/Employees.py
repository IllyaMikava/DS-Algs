class Employee:
    def __init__(self, fname, lname, email) -> None:
        self.fname = fname
        self.lname = lname
        self.email = email

    def display(self):
        message = f'{self.fname} {self.lname} {self.email}'
        return message
    
    def __str__(self):
        return self.display()