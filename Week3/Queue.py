class IQueue:
    def enq(self, name, secondname, email, time):
        raise NotImplementedError("enq() needs to be implemented")
    def deq(self):
        raise NotImplementedError("deq() needs to be implemented")
    def peek(self):
        raise NotImplementedError("peek() needs to be implemented")
    def size(self):
        raise NotImplementedError("size() needs to be implemented")
    def is_empty(self):
        raise NotImplementedError("is_empty() needs to be implemented")
    def print_all(self):
        raise NotImplementedError("print_all() needs to be implemented")