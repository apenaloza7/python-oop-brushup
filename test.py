from Models.Employee import *
from Models.Manager import *

# Test file used to test my methods as I go along

emp_1 = Employee('Alejandro', 'Penaloza', 'Software', 100000)
manager_1 = Manager('Alex', 'Penaloza', 'Software', 120000, 'Software', [emp_1])

print(manager_1.annual_raise_amount)
manager_1.add_employee(emp_1)
print(manager_1.print_employees())
