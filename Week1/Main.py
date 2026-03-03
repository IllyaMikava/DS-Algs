from Students import Student
from Course import Course

# Create an instance of the Course class for TU850
tu850 = Course(
    course_title = "BSc in Computer Science",
    course_code = "TU850",
    award = "Bachelor of Science",
    nfq_level = 8
)

# Create 4 students with meaningful data
student1 = Student(
    fname = "John",
    lname = "Murphy",
    id="C00123456",
    year=2,
    email="john.murphy@student.tu.ie",
    pps="1234567AB",
    middleName="Patrick"
)

student2 = Student(
    fname="Sarah",
    lname="O'Brien",
    id="C00234567",
    year=2,
    email="sarah.obrien@student.tu.ie",
    pps="2345678CD",
    middleName="Marie"
)

student3 = Student(
    fname="Michael",
    lname="Kelly",
    id="C00345678",
    year=2,
    email="michael.kelly@student.tu.ie",
    pps="3456789EF",
    middleName="James"
)

student4 = Student(
    fname="Sarah",
    lname="O'Brien",
    id="C00234567",
    year=2,
    email="sarah.obrien@student.tu.ie",
    pps="2345678CD",
    middleName="Marie"
)

# Add students to the course
tu850.add_student(student1)
tu850.add_student(student2)
tu850.add_student(student3)
tu850.add_student(student4)

# Display all students on the course
tu850.display_all_students()

# Demonstrate using getters and setters
print("\nDemonstrating getters and setters:")
print(f"First student's email: {student1.get_email()}")
student1.set_email("j.murphy@student.tu.ie")
print(f"Updated email: {student1.get_email()}")