from student_grade_list import StudentGradeList

grade_list = StudentGradeList()
grade_list.add_student("Illya", "Ilya@gmail.com", 99)
grade_list.add_student("tim", "Illya@gmail.com", 98)
grade_list.add_student("kai", "I@gmail.com", 20)
grade_list.add_student("jon", "a@gmail.com", 30)
grade_list.add_student("kit", "ya@gmail.com", 9)


student = grade_list.search("Ilya@gmail.com")
print(student)

# delete_email = "Ilya@gmail.com"
# is_deleted = grade_list.delete_student(delete_email)
# print(f"{delete_email} was deleted: {is_deleted}")

highest_grade_list = grade_list.highest_grade()
print(highest_grade_list)

size = grade_list.size()
print("Number of students:", size)