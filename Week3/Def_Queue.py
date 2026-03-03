from Queue import IQueue
from datetime import datetime

class Queue(IQueue):
    def __init__(self, max = 0) -> None:
        self.__storage = []
        self.__maxsize = max

    def enq(self, name, secondname, email): 
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        student = (name, secondname, email, time)
        self.__storage.append(student)
        return student
    
    def deq(self):
        if self.is_empty():
            return None
        return self.__storage.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.__storage[0]

    def size(self):
        return len(self.__storage)

    def is_empty(self):
        return len(self.__storage) == 0
    
    def print_all(self):
        print("\nCurrent items on the q:")
        for student in self.__storage:
            print(student)
        