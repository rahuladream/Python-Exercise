"""
Finding prime number 
Constraints 
1 <= N <= 1000
"""

input = int(input())
for i in range(2,input):
	if i > 1:
		for j in range(2, i):
			if (i % j) == 0:
				break
		else:
			print(i, end=" ")
