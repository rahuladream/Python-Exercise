#!/bin/python
"""
Find the number of string to be removed to make both 
words anagram
"""

import string
t=int(input())
for _ in range(t):
	s1 = input()
	s2 = input()
	c=0
	for i in string.ascii_lowercase:
		c+=abs(s1.count(i)-s2.count(i))
	print(c)
