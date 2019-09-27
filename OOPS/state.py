"""
One way to do that is by using global state
"""

balance = 0

def deposit(amt):
	global balance
	balance += amt
	return balance

def withdraw(amt):
	global balance
	balance -= amt
	return balance


"""
What if We have multiple bank account, the problem solved by making
the state local, probably by using a dictionary to store the state.
"""

def make_account():
	return {'balance' : 0}

def deposit(account, amount):
	account['balance'] += amount
	return account['balance']

def withdraw(account, amount):
	account['balance'] -= amount
	if account['balance'] >= 0:
		return account['balance'] = 0


if __name__ == '__main__':
	a = make_account()
	# User a and b created an account
	b = make_account()

	deposit(a, 100)
	print("User A Balance {}".format(a))
	deposit(b, 50)
	print("User B Balance {}".format(b))
	withdraw(b, 60)
	print("User B Balance after withdraw {}".format(b))
	withdraw(a, 10)
	print("User A Balance after withdraw {}".format(a))