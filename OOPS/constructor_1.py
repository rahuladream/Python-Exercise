"""
Special function gets called whenever a new object of that class is initiated.

This type of function is also called constructots in OOP.
We normally use to initialize all the variables.

"""

class ComplexNumber:
	def __init__(self, r=0, i=0):
		self.real = r
		self.imag = i

	def getData(self):
		print("{} + {}".format(self.real, self.imag))

# Create a new object ComplexNumber
c1 = ComplexNumber(2,3)
c1.getData()

# Another complexNumber object
c2 = ComplexNumber(5)
c2.attr = 10
print(c2.real, c2.imag, c2.attr)

c1.attr