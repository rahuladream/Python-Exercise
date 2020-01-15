"""
QUESTION 1:
Swap the case of the string that comes as an input and return the string while making sure that the first letter of the string stays Uppercase.
Example -

Input - "PyThON"

Output - "PYtHon"
"""


def main(i):
	res = ""
	swap = i.swapcase()
	for i in range(len(swap)):
		if i == 0:
			res = res + swap[i].upper()
		else:
			res = res +  swap[i] 
	return res

print(main('RaHuL'))