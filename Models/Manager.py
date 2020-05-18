from Models.Employee import *

# Manager Model
#
# Author: Alejandro Penaloza
# Last Updated: May 17 2020
#
# Sub-class of Employee model

def manager(Employee):

     annual_raise_amount = 1.14

     # creates instance of a manager
     def __init__(self, firstName, lastName, dept, salary, deptManaged):
         super().__init__(firstName, lastName, dept, salary)
         self.deptManaged = deptManaged
