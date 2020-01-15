def main(i):
	res = ""
	swap = i.swapcase()
	for i in range(len(swap)):
		if i == 0:
			res = res + swap[i].upper()
		else:
			res = res +  swap[i] 
	return res

print(main('RaHuL'))