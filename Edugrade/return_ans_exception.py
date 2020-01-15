"""
QUESTION 5:
Give 2 no.s A and B return (A+B)/(A-B). In case of an exception return 0

Example -

Input - 7,2

Output - 1.8

explanation - 7+2/7-2 => 1.8
"""

def main(i,j):
	try:
		res = (i + j)/(i - j)
	except:
		res = 0
	return res

print(main(-1,-1))
