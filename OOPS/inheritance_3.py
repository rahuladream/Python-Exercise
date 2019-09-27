"""
A polygon is a closed figure with 3 or more sides. Say we have a class called Polygen


isinstance() and issubclass() are use to check inheritance.

Function isinstance() returns True if the object is an instance of the class or other classes derived from it.


Function issubclass() is used to check for the class inheritance
"""

class Polygen:
	def __init__(self, no_of_sides):
		self.n = no_of_sides
		self.sides = [0 for i in range(no_of_sides)]

	def inputSides(self):
		self.sides = [float(input("Enter sides "+str(i+1)+" : ")) for i in range(self.n)]

	def dispSides(self):
		for i in range(self.n):
			print("Side", i+1, "is", self.sides[i])


class Triange(Polygen):
	def __init__(self):
		Polygen.__init__(self,3)

	def findArea(self):
		a,b,c = self.sides
		s = (a + b + c) / 2
		area = (s*(s - a)*(s - b)*(s - c)) ** 0.5
		print('The are of the triangle is %0.2f' %area)

if __name__ == '__main__':
	t = Triange()
	t.inputSides()
	t.dispSides()
	t.findArea()


"""
OUTPUT:

Enter sides 1 : 3
Enter sides 2 : 5
Enter sides 3 : 4
Side 1 is 3.0
Side 2 is 5.0
Side 3 is 4.0
The are of the triangle is 6.00

"""