"""
A concept of using common operations in different ways for 
different user input
"""

class Parrot:
	def fly(self):
		print("Parrot can fly")

	def swim(self):
		print("Parrot can't swim")

class Penguin:
	def fly(self):
		print("Penguin can't fly")

	def swim(self):
		print("Penguid can't swim")

# Common Interface

def flying_test(bird):
	bird.fly()


blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)