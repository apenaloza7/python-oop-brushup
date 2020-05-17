# Employee Modal
#
# Author: Alejandro Penaloza
# Last Updated: May 16 2020

class Employee:

    # creates an instance of an Employee
    def __init__(self, firstName, lastName, dept, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.dept = dept
        self.salary = salary
        self.email = firstName + '.' + lastName + '@apenaloza.com'

    def fullName(self):
        return '{} {}'.format(self.firstName, self.lastName)
