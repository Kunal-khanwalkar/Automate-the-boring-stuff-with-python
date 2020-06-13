import csv
from collections import Counter
import math


def info(D):
	
	column = []	
	for i in range(1,len(D)):
		column.append(D[i][-1])
	
	keys = Counter(column).keys()
	values = Counter(column).values()
	entries = len(column)	

	print('Keys:',list(keys))
	print('Values:',list(values));
	print('Entries:',entries)

	result = 0
	for i in values:
		result -= (i/entries)*math.log2(i/entries)

	return round(result,4)


def I(args):	
	entries = sum(args)

	result = 0
	for i in args:
		result -= (i/entries)*math.log2(i/entries)

	return round(result,4)


def info_class(D,c):

	cl = D[0][c]	
	column = []	
	output = []
	for i in range(1,len(D)):
		column.append(D[i][c])
		output.append(D[i][-1])
	
	keys = list(Counter(column).keys())
	values = list(Counter(column).values())
	entries = len(column)		

	print('Keys:',keys)
	print('Values:',values)
	print('Total entries:',entries)

	result = 0
	for i in range(len(keys)):
		temp = []
		for j in range(len(column)):
			if(keys[i]==column[j]):
				temp.append(output[j])		
		new_values = list(Counter(temp).values())				
		print('I('+str(new_values)+')',end='+')
		result += (values[i]/entries)*I(new_values)
	print()
	return round(result,4)


def split_info(D,c):

	cl = D[0][c]	
	column = []	
	output = []
	for i in range(1,len(D)):
		column.append(D[i][c])
		output.append(D[i][-1])
	
	keys = list(Counter(column).keys())
	values = list(Counter(column).values())
	entries = len(column)		

	result = 0
	for i in values:
		result -= (i/entries)*math.log2(i/entries)

	return round(result,4)




def gain(info1,info2):
	return round(info1-info2,4)

def gain_ratio(G,S):
	return round(G/S,4)


def printMatrix(matrix):
	for i in matrix:
		print(i)


def readinput():
	fileInputStream = open('.\\classification_input.csv','r')
	reader = csv.reader(fileInputStream,delimiter=',')
	return [row for row in reader]


def main():
	print('Input D:\n')
	D = readinput()			
	printMatrix(D)		

	print('\n Info(D): ')
	Inf = info(D)
	print(Inf)	

	gains = []

	print('\nInfo for all classes\n')
	for i in range(len(D[0])-1):
		print('\n',D[0][i])
		I = info_class(D,i)
		print('class Info: ',I)
		S = split_info(D,i)		
		print('Split Info: ',S)
		G = gain(Inf,I)
		print('Gain: ',G)
		Gr = gain_ratio(G,S)
		print('Gain ratio: ',Gr)
		gains.append(G)

	print('\nClass with maximum gain: ', D[0][gains.index(max(gains))])	

if __name__=='__main__':
	main()