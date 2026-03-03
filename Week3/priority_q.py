from i_priority_q import PriorityQueue

class PriorityQueue(PriorityQueue):
    def __init__(self):
        self.__storage = []

    def enq(self, obj, priority):
        self.__storage.append((priority, obj))

    def deq(self):
        """Remove and return the patient with the highest priority."""
        if not self.__storage:
            return None

        # Find the patient with the highest priority
        highest_priority = -1
        index = -1
        for i, (priority, obj) in enumerate(self.__storage):
            if priority > highest_priority:
                highest_priority = priority
                index = i

        # Remove and return the patient
        _, patient_obj = self.__storage.pop(index)
        return patient_obj

    def peek(self):
        """Return the patient with the highest priority without removing."""
        if not self.__storage:
            return None
        return max(self.__storage, key=lambda x: x[0])[1]

    def size(self):
        return len(self.__storage)

    def is_empty(self):
        return len(self.__storage) == 0

    def print_all(self):
        for priority, obj in self.__storage:
            print(f"Priority: {priority}, {obj}")