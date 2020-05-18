# Employee Model
#
# Author: Alejandro Penaloza
# Last Updated: May 16 2020

class Employee:

    annual_raise_amount = 1.07

    # creates an instance of an Employee
    def __init__(self, firstName, lastName, dept, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.dept = dept
        self.salary = salary

    # returns the full name of employee
    def fullName(self):
        return '{} {}'.format(self.firstName, self.lastName)

    # returns all of the information about an employee
    def completeInfo(self):
        return '{} {} {} {} {}'.format(self.firstName, self.lastName, self.dept, self.salary, self.email)

    # applies raise to given employee
    def apply_raise(self):
        self.pay = int(self.pay * self.annual_raise_amount)

    # sets the email for the employee
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.firstName, self.lastName).lower()


    """ ----------------------- CLASS METHODS ----------------------- """

    # changes the annual raise amount
    @classmethod
    def set_raise_amount(cls, amount):
        cls.annual_raise_amount = amount

    # serves as an alternative constructor for creating an employee given
    # a string where commas are the seperators
    @classmethod
    def from_string_commas(cls, empString):
        firstName, lastName, dept, salary = empString.split(',')
        return cls(firstName, lastName, dept, salary)

    # serves as an alternative constructor for creating an employee given
    # a string where dashes are the seperators
    @classmethod
    def from_string_dashes(cls, empString):
        firstName, lastName, dept, salary = empString.split('-')
        return cls(firstName, lastName, dept, salary)

    # serves as an alternative constructor for creating an employee given
    # a string where underscores are the seperators
    @classmethod
    def from_string_underscores(cls, empString):
        firstName, lastName, dept, salary = empString.split('_')
        return cls(firstName, lastName, dept, salary)

    """ ----------------------- STATIC METHODS ----------------------- """

    # returns false if the day falls on the weekend
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
