class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def print(self):
        print("Name: {} Age: {}".format(self.name, self.age))


class Employee(Person):
    def __init__(self, name, age, position, salary):
        Person.__init__(self, name, age)
        self.position = position
        self.salary = salary
    
    def print(self):
        Person.print(self)
        print("Salary: {} Position: {}".format(self.salary, self.position))

class Enterprenaur(Person, Employee):
   pass


