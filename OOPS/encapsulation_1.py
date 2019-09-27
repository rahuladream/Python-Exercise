"""
Way of hiding the private details of a class from other objects
"""

class Computer:
	def __init__(self):
		self.__maxprice = 900

	def sell(self):
		print("Sellingprice : {}".format(self.__maxprice))

	def setMaxPrice(self, price):
		self.__maxprice = price


c = Computer()
c.sell()

# Change the price 
# (Tried to change the data but we are not able to change the original data that's the power of encapsulation)
c.__maxprice = 1000
c.sell()

# Using setter function
c.setMaxPrice(1000)
c.sell()