"""
Let create little bit more sophisticate account type where we come up with old problem 
that the balance is going in minus
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


class MinimumBalance(BankAccount):
	def __init__(self, min_balance):
		BankAccount.__init__(self)
		self.min_balance = min_balance

	def withdraw(self, amount):
		if self.balance - amount < self.min_balance:
			print('Sorry, minimum balance must be maintained')
		else:
			BankAccount.withdraw(self, amount)


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