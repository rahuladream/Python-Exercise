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