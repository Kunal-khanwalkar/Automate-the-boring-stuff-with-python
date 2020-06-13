import csv
import math


def euclidean_distance(a1,b1):
	result = math.sqrt((a1[0]-b1[0])**2 + (a1[1]-b1[1])**2)
	return round(result,4)

def average(a1):

	x = 0
	y = 0

	for i in a1:
		x += i[0]
		y += i[1]

	x = x/len(a1)
	y = y/len(a1)

	return (x,y)


def printMatrix(matrix):
	for i in matrix:
		print(i)


def readinput():
	fileInputStream = open('.\\kmeans_input.csv','r')
	reader = csv.reader(fileInputStream,delimiter=',')
	return [[row[0],(float(row[1]),float(row[2]))] for row in reader]


def defineK():
	k = int(input('Enter value of k: '))

	centres = []
	for i in range(k):
		print('Enter coordinates for Centre',i+1)
		x = float(input('x: '))
		y = float(input('y: '))
		centres.append((x,y))

	return k,centres


def kmeans(D,centres,k):

	print('\nTable:')
	cluster_list = []

	for i in D:
		getdist = []
		for j in centres:						
			getdist.append(euclidean_distance(i[1],j))		
		print(i,getdist,getdist.index(min(getdist)))
		cluster_list.append(getdist.index(min(getdist)))
	
	clusters = {new_list: [] for new_list in range(k)}


	print('\nClusters: ')
	for i in range(len(D)):		
		clusters[cluster_list[i]].append(D[i][1])
	print(clusters)


	new_centres = []
	for key,val in clusters.items():
		new_centres.append(average(val))

	return new_centres





def main():	
	print('Input D:\n')
	D = readinput()			
	printMatrix(D)	
	
	k,centres = defineK()
	print('\nCurrent centres: \n')	
	printMatrix(centres)

	iterations = int(input('No of iterations: '))


	for i in range(iterations):			
		new_centres = kmeans(D,centres,k)
		print('\nNew centres: ')
		printMatrix(new_centres)
		centres = new_centres



if __name__=='__main__':
	main()