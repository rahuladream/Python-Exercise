#!/bin/python
"""
User will enter the file name and you are required to read that file and print the number of words in it.
"""

file = open(input("Enter file name: "), 'r')
c=0
for line in file:
	for word in line.split(" "):
		c+=1
	print(c)

