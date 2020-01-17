"""
Read the file 'test.csv' and change the Grade of Rohit's grade to A and save the file to 'test.csv'

Example -

Read -  Name,Class,Subject,Grade
        Ajay,   10, English,A
        Rohit,  9,  English,B
        Chaman, 10, English,A
        Rudra,  9,  English,C
        Rajesh, 10, English,B

Write - Name,Class,Subject,Grade
        Ajay,   10, English,A
        Rohit,  9,  English,A
        Chaman, 10, English,A
        Rudra,  9,  English,C
        Rajesh, 10, English,B

Explanation read the csv file and then store the data into local variable and again write that data using writerow function of csv module (Note: Don't forget to use 
newlin='' when opening the csv file in write mode)
"""
import csv
def main():
	# Write your code here and return the output
	new_txt = []
	text = open('test.csv', "r")
	line = 0
	for val in text:
		if line == 0:
			new_txt.append(val)
		else:
			x, y, z, a = val.split(',')
			if x == 'Rohit':
				new_txt.append(val.replace("B","A"))
			else:
				new_txt.append(val)
		line += 1
	x = open('output.csv', "w")
	x.writelines(new_txt)
	x.close()

if __name__ == '__main__':
	main()