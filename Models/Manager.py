from .Employee import *

# Manager Model
#
# Author: Alejandro Penaloza
# Last Updated: May 17 2020
#
# Sub-class of Employee model

class Manager(Employee):

    annual_raise_amount = 1.14

    # creates instance of a manager
    def __init__(self, firstName, lastName, dept, salary, deptManaged, employees = None):
        super().__init__(firstName, lastName, dept, salary)
        self.deptManaged = deptManaged

        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    # allows for the addition of managed employees
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    # allows for the removal of managed employees
    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    # prints the employees onto the terminal
    def print_employees(self):

        # counter for the displaying of employees
        employee_counter = 1

        for emp in self.employees:
            print(str(employee_counter) + ') '  + emp.fullName() + '\n')
            employee_counter += 1

        # resets the counter back to one after the for-loop is over
        employee_counter = 1
