"""
QUESTION 2:
You will get a list in input consisting of only tuple elements. Each tuple will have 2 numeric elements. You have to return the maximum difference between the tuple pairs

Example -

Input - [(10,12),(8,15),(20,8),(2,-10)]

Output - 12

Reason - The difference between all the tuple pairs are 2,7,12,12 respectively and max of them is 12.
"""

def main(i):
	odd = 0
	even = 0
	for val in i:
		if val % 2 == 0:
			even += 1
		else:
			odd += 1
	tmp = [odd, even]
	return tuple(tmp)

print(main([2,3,4,5,6,7,8]))