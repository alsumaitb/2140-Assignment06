# Assignment 06, Question 03

class Employee:
    
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    def calculate_salary(self):
        print("Employee.calculate_salary")
        
class HourlyEmployee(Employee):
    def __init__(self, name, position, hourly_rate):
        super().__init__(name, position)
        self.hourly_rate = hourly_rate
        
    def calculate_salary(self):
        salary = 40*self.hourly_rate
        print(f"The salary for the hourly employee is {salary}")
    
class SalariedEmployee(Employee):
    def __init__(self, name, position, salary):
        super().__init__(name, position)
        self.salary = salary
    
    def calculate_salary(self):
        print(f"The salary for the salaried employee is {self.salary}")
        
class ComissionEmployee(Employee):
    def __init__(self, name, position, sales, commission_rate):
        super().__init__(name, position)
        self.sales = sales
        self.commission_rate = commission_rate
        
    def calculate_salary(self):
        salary = self.sales*self.commission_rate
        print(f"The salary of the commission employee is {salary}")
        
def main():
    
    employee1 = HourlyEmployee("Bader", "Manager", 30)
    employee2 = SalariedEmployee("Omkar", "TA", 75000)
    employee3 = ComissionEmployee("Julian", "Real Estate Agent", 100000, 0.1)
    
    mylist = [employee1, employee2, employee3]
    
    for a in mylist:
        a.calculate_salary()
        
main()
    
    
    
    
        
    
