"""
It is as easy as defining a normal function with yield statement instead of a return statement.

If a function contains at least one yield statement (it may contain other yield or return statements), it becomes a generator function. Both yield and return will return some value from a function.

The difference is that, while a return statement terminates a function entirely, yield statement pauses the function saving all its states and later continues from there on successive calls.


1. Generator function contains one or more yield statement.
2. When called, it returns an object (iterator) but does not start execution immediately.
3. Methods like __iter__() and __next__() are implemented automatically. So we can iterate through the items using next().

"""

def gen():
	n = 1
	print('This is printed first')
	yield n

	n += 1
	print('This is printed secondly')
	yield n

	n += 1
	print('This is printed last')
	yield n


def rev_str(string):
	length = len(string)
	for i in range(length - 1 , -1, -1):
		yield string[i]


for char in rev_str("Rahul"):
	print(char, end=" ")
print("\n")


for item in gen():
	print(item)


