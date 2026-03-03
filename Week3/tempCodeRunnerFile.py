from my_stack import MyStack
from Employees import Employee

hr = MyStack()

e1 = Employee('illya', 'mikava', 'lwskdjnc@gmail.com')
e2 = Employee('jane', 'mikava', 'lwskdjnc@gmail.com')
e3 = Employee('tim', 'mikava', 'lwskdjnc@gmail.com')

hr.push(e1)
hr.push(e2)
hr.push(e3)

hr.print_all()

fire = hr.pop()
print(f'we had to fire {fire.display()}')
fire = hr.pop()
print(f'we had to fire {fire.display()}')
fire = hr.pop()
print(f'we had to fire {fire.display()}')