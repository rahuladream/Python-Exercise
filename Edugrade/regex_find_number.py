"""
Given an string input find all the no.s in the string using regular expression. If there are more than one no. present return a list containing all the no.s

Example -

Input - "There are 12 dogs and 7 cats in the house."

Output - ['12','7']
"""

import re
def main(i):
	res = re.findall(r'\d+', i)
	return res

print(main("There are 12 dogs and 7 cats in the house."))