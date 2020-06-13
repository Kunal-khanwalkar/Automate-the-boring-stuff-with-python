import csv


def manhattan_distance(a1,b1):
	result = abs(a1[0]-b1[0]) + abs(a1[1]-b1[1])
	return round(result,4)


def printMatrix(matrix):
	for i in matrix:
		print(i)


def readinput():
	fileInputStream = open('.\\pam_input.csv','r')
	reader = csv.reader(fileInputStream,delimiter=',')
	return [[row[0],(int(row[1]),int(row[2]))] for row in reader]

def defineK():
	k = int(input('Enter value of k: '))

	centres = []
	for i in range(k):
		print('Enter coordinates for Centre',i+1)
		x = int(input('x: '))
		y = int(input('y: '))
		centres.append((x,y))

	return k,centres



def pam(D,centres,k):

	print('\nTable:')

	dissimilarities = {new_list: [] for new_list in range(k)}

	for i in D:
		for j in range(len(centres)):
			dissimilarities[j].append(manhattan_distance(i[1],centres[j]))

	print('\nDissimilarities: ')
	print(dissimilarities)

	min_centres = {new_list: [] for new_list in range(k)}

	for i in range(len(D)):
		templ = []
		for j in range(len(centres)):
			templ.append(dissimilarities[j][i])
		min_centres[templ.index(min(templ))].append(i)

	print('\nMinimum centres: ')
	print(min_centres)

	S = 0
	for key,val in min_centres.items():
		for i in val:
			S += dissimilarities[key][i]

	print('\nS: ',S)




def main():
	print('Input D:\n')
	D = readinput()			
	printMatrix(D)	

	k,centres = defineK()
	print('\nCurrent centres: \n')	
	printMatrix(centres)

	pam(D,centres,k)



if __name__=='__main__':
	main()