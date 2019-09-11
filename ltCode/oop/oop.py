class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('ge', 'ds', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# emp_1.fullname()
# Employee.fullname(emp_1)  are same
