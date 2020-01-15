"""
Given an array of elements N return the count of odd and even no.s using lambda function

Example -

Input - [2,3,4,5,6,7,8]

Output -(3,4)

Explanation - There are 3 odd no.s and 4 even no.s in the list.
"""

def main(i):
	tmp = []
	for k,v in i:
		tmp.append(abs(v - k))
	return max(tmp)


print(main([(10,12),(8,15),(20,8),(2,-10)]))