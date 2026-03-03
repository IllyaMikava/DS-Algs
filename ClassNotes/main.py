from priority_queue import PriorityQueue
from patient import patient

pq = PriorityQueue()

sick = [
        ("John", "Doe", "1234567A", "Broken Arm", 3),
        ("ilya", "oooo", "124567A", "Broken leg",6),
        ("kai", "eeee", "1234A", "Broken brain",9)
    ]

# p1 = patient("John", "Doe", "1234567A", "Broken Arm")
# p2 = patient("ilya", "oooo", "124567A", "Broken leg")
# p3 = patient("kai", "eeee", "1234A", "Broken brain")


for s in sick:
    fname, lname, pps, injury, priority = s
    p = patient(fname, lname, pps, injury)
    pq.enq(p, priority)

print("All patients in the queue:")
pq.print_all() 

print("\nsize of queue: ", pq.size())

print("\nDequeuing patients by priority:")
while not pq.is_empty():
    patient = pq.deq()
    print(patient)

print("\nsize of queue: ", pq.size())



