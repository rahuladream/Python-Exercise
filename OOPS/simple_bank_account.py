"""
Model a bank accoubnt class
Reference : purcellconsult
"""

class BankAccount:
	def __init__(self, fname, lname, account_num):
		self.fname = fname
		self.lname = lname
		self.account_num = account_num
		self.balance = 0
		self.transactions = []

	def deposit(self, amount):
		self.balance += amount
		self.transactions.append(+amount)
		return amount

	def withdraw(self, amount, limit=1000):
		if self.balance - amount > 0 and amount <= limit:
			self.balance -= amount
			self.transactions.append(-amount)
			return amount
		else:
			return 'Your withdrawal amount is ₹{} which exceeds your account limit! You have:' \
                   '₹{}. Your withdrawal limit is {}'.format(amount, self.balance, limit)

	def get_first_name(self):
	    return self.fname
	def get_last_name(self):
	    return self.lname
	def get_account_num(self):
	    return self.account_num
	def get_balance(self):
	    return self.balance
	def recent_transactions(self):
		if len(self.transactions) < 1:
			return None
		else:
			return self.transactions.pop()


if __name__ == '__main__':
	a = BankAccount('Rahul', 'Singh', 3628902828)
	print('first name =', a.get_first_name())
	print('last name =', a.get_last_name())
	print('account number =', a.get_account_num())
	print('account balance =', a.get_balance())
	print('deposit =', a.deposit(20))
	print('recent transaction is:', a.recent_transactions())
	print('account balance =', a.get_balance())
	print('withdrawal =', a.withdraw(50))
	print('recent transaction is =', a.recent_transactions())
	print('account balance =', a.get_balance())
	print('deposit =', a.deposit(500))
	print('withdrawal =', a.withdraw(891))
	print('recent transaction is =', a.recent_transactions())
	print('withdrawal =', a.withdraw(49))
	print('recent transaction is =', a.recent_transactions())
	print('Final Balance is = ', a.get_balance())