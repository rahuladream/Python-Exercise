"""
A process of using details from a new class without modifying existing class
"""

class Bird:
	def __init__(self):
		print("Bird is ready")

	def whoisThis(self):
		print("Bird")

	def swim(self):
		print("Swim faster")

class Penguin(Bird):
	def __init__(self):
		super().__init__()
		print("Penguin is ready")

	def whoisThis(self):
		print("Penguin")

	def run(self):
		print("Run Faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()


"""
OUTPUT:

Bird is ready
Penguin is ready
Penguin
Swim faster
Run Faster

"""