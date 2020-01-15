"""You will get a number in input you have to get all the prime no.s till that no

Example -

Input - 10

Output -[2,3,5,7]

Explanation - First element of input list is 4 so multiply the whole list by 4 and return the output list."""


def main(i):
	arry = []
	for i in range(2,i):
		if i > 1:
			for j in range(2, i):
				if (i % j) == 0:
					break
			else:
				arry.append(i)
	return arry

print(main(10))

