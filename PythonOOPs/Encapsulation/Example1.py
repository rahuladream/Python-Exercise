class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def name(self):
        print("Name of Person is {}".format(self.name))

    def _age(self):
        '''
        Protected member is written by single dash(_)
        and can't be accessible by child class
        '''
        print('Age of human {}'.format(self.age))
    
    def __salary(self):
        '''
        Private member is written by double dash(__)
        and can't access by child class
        '''
        print("Salary of person is {}".format(self.salary))

class Employee(Person):
    def __init__(self, name,age,salary,position):
        Person.__init__(self, name, age,salary)
        self.position = position
    
    def tell(self):
        Person.name(self)
        # Person._age(self)
        # Person.__salary(self)
        print("Position: {}".format(self.position))



if __name__ == '__main__':
    p = Employee("Rahul", 13, 50000, "Software Engineer")
    p.tell()