class Employee:
    
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Raghav','Sarda',50000 )
emp_2 = Employee('Test','User',60000 )

print(emp_1.__dict__)
print(Employee.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

Employee.raise_amount = 1.05
print(' ')
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


print(' ')
print(emp_1.__dict__)

emp_1.raise_amount = 1.06

print(emp_1.__dict__)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)