class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def tell(self):
        print("Name: {} Age:{}".format(self.name, self.age))
    

class Employee:
    def __init__(self, position, salary):
        self.position = position
        self.salary = salary

    def tell(self):
        print("Position: {} Salary: {}".format(self.position, self.salary))
 

class Enterprenaur(Person, Employee):
    def __init__(self, name, age, salary, position, exp):
        self.exp = exp
        Person.__init__(self, name, age)
        Employee.__init__(self, position, salary)
    
    def print(self):
        Person.tell(self)
        Employee.tell(self)
        print("Experience {}".format(self.exp))

if __name__ == "__main__":
    obj = Enterprenaur("Rahul", 30, 133410, 'HR', 10)
    obj.print()
