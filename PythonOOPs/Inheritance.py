class SchoolMember:
    ''' Represents any school member '''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Initialized school member: {}'.format(self.name))

    def tell(self):
        ''' Tell my details '''
        print('Name: {} Age: {}'.format(self.name, self.age))


class Teacher(SchoolMember):
    ''' Represents any teacher '''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('Initialized teacher: {}'.format(self.name))

    def tell(self):
        ''' Tell my details '''
        SchoolMember.tell(self)
        print('Salary: {}'.format(self.salary))
    
class Student(SchoolMember):
    ''' Represents any student '''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('Initialized student'. format(self.name))
    
    def tell(self):
        SchoolMember.tell(self)
        print('Marks: {}'.format(self.marks))


t = Teacher('Mrs. Shrividiya', 40, 3000)
s = Student('Swaroop', 25, 300)

print()

members = [t, s]

for member in members:
    member.tell()