#!/bin/python
"""
Finding the fibnocci series and also it
using map and lamba expression
"""

cube = lambda x: x ** 3 # complete the lambda function 

def fibonacci(n):
	fib = [0,1]
	for _ in range(2,n):
		fib.append(fib[-1] + fib[-2])
	return fib
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))