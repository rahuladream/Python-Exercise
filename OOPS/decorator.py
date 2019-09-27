"""
Function that take other functions as arguments are also called higher order functions. 

Python has an interesting feature called decorators to add functionality to an existing code.

This is also called metaprogramming as a part of the program tries to modify another part of the program at compile time.
"""

def smart_divide(func):
	def inner(a,b):
		print("I am going to divide", a, "and",b)
		if b == 0:
			print("Whoops! cannot divide")
			return
		return func(a,b)
	return inner

@smart_divide
def divide(a,b):
	return a/b


print(divide(2,5))

print(divide(2,0))



def star(func):
	def inner(*args, **kwargs):
		print("*" * 30)
		func(*args, **kwargs)
		print("*" * 30)
	return inner

def percent(func):
	def inner(*args, **kwargs):
		print("%" * 30)
		func(*args, **kwargs)
		print("%" * 30)
	return inner

@star
@percent
def printer(msg):
	print(msg)
printer("Hello")