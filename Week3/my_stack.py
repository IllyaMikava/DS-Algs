from i_stack import Istack

class MyStack(Istack):
    def __init__(self) -> None:
        self.__storage = []

    def push(self, obj):
        self.__storage.append(obj)

    def pop(self):
        if len(self.__storage) == 0:
            return None
        return self.__storage.pop(-1)
    
    def peek(self):
        if len(self.__storage) == 0:
            return None
        return self.__storage(-1)
        
    def size(self):
        return len(self.__storage)

    def is_empty(self):
        if len(self.__storage) == 0:
            return True
        else:
            return False

    def print_all(self):
        print("current items on the stack:")
        for employee in self.__storage:
            print(employee)