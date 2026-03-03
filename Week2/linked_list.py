class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:  # List is empty
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:  # Empty list
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    # Remove at beginning
    def remove_at_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head == self.tail:  # Only one node
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

    # Remove at end
    def remove_at_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head == self.tail:  # One node
            self.head = None
            self.tail = None
            return

        current = self.head
        while current.next != self.tail:
            current = current.next

        current.next = None
        self.tail = current

    # Print list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")