from Def_Queue import Queue

q = Queue()

# q.enq("illya Mikava")
# q.enq("Hello Mikava")
# q.enq("Tom Mikava")


students = [
    ("Illya", "Mikava", "illya@gmail.com"),
    ("Tom", "Smith", "tom@gmail.com"),
    ("Anna", "Brown", "anna@gmail.com"),
    ("John", "White", "john@gmail.com"),
    ("Kate", "Black", "kate@gmail.com"),
    ("Mark", "Green", "mark@gmail.com"),
    ("Sara", "Gray", "sara@gmail.com"),
    ("Luke", "Blue", "luke@gmail.com"),
    ("Emma", "Gold", "emma@gmail.com"),
    ("Leo", "Silver", "leo@gmail.com")
]

for s in students:
    q.enq(s[0], s[1], s[2])


q.print_all()

print("\nNext to demo:")
print(q.peek())

if(q.enq("John", "White", "john@gmail.com")):
    print("\nadded sucessfully")

q.print_all()

if(q.deq()):
    print("\ndequued sucessfully")

q.print_all()


print("\n", q.size())

print("\nNext to demo:")
print(q.peek())

if(q.deq()):
    print("\ndequued sucessfully")

q.print_all()

print("\n", q.size())




