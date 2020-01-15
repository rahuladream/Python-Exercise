def main(i):
	tmp = []
	for k,v in i:
		tmp.append(abs(v - k))
	return max(tmp)


print(main([(10,12),(8,15),(20,8),(2,-10)]))