"""
Bank account example with class and objects
"""

class BankAccount:
	def __init__(self):
		self.balance = 0

	def deposit(self, amount):
		self.balance += amount
		return self.balance

	def withdraw(self, amount):
		self.balance -= amount
		return self.balance


if __name__ == '__main__':
	a = BankAccount()
	b = BankAccount()

	a.deposit(100)
	print("User A Balance {}".format(a.balance))
	b.deposit(50)
	print("User B Balance {}".format(b.balance))
	b.withdraw(60)
	print("User B Balance after withdraw {}".format(b.balance))
	a.withdraw(10)
	print("User A Balance after withdraw {}".format(a.balance))