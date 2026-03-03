from Employees import Employee
from priority_q import PriorityQueue

pq = PriorityQueue()

sick = [
        ("John", "Doe", 3),
        ("ilya", "oooo",6),
        ("kai", "eeee", 9)
    ]

for s in sick:
    fname, lname, priority = s
    p = Employee(fname, lname, priority)
    pq.enq(p, priority)

pq.print_all()