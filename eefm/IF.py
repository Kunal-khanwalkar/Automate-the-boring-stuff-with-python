import csv
import re
import parser


interests = ['0.25','0.5','0.75','1.0','1.25','1.5','1.75','2.0','3.0','4.0','5.0','6.0','7.0','8.0','9.0','10.0','11.0','12.0','13.0','14.0','15.0','16.0','18.0','20.0','25.0','30.0','35.0','40.0','50.0']
headings = ['Compound Amount Factor','Present Worth Factor','Compound Amount Factor','Sinking Fund Factor','Present Worth Factor','Capital Recovery Factor','Gradient Uniform Series','Gradient Present Worth']
Formulae = ['(F/P,i,n)','(P/F,i,n)','(F/A,i,n)','(A/F,i,n)','(P/A,i,n)','(A/P,i,n)','(A/G,i,n)','(P/G,i,n)']



def createFiles():	

	for i in interests:
		filenm = '.\\data\\' + i + '.csv'
		with open(filenm,'w',newline='') as file:
			writer = csv.writer(file)
			writer.writerow(headings)
			writer.writerow(Formulae)




def cleanFile():

	input_file = '.\\Text_IF_Table.txt'
	output_file = '.\\New_IF_Table.csv'

	data = list(csv.reader(open(input_file,'r')))


	with open(output_file,'w',newline='') as file:
		writer = csv.writer(file)

		for line in data:
			if(re.search('[a-zA-Z%]',line[0]) == None):				
				getstr = [float(element) for element in line[0].split(' ')]				
				print(line[0])
				writer.writerow(getstr)




def populateFiles():

	input_file = '.\\New_IF_Table.csv'
	data = list(csv.reader(open(input_file,'r')))

	interest_cnt = -1

	for line in data:
		if float(line[0])==1.0:
			interest_cnt += 1
			output_file = '.\\data\\' + interests[interest_cnt] + '.csv'			
		
		with open(output_file,'a',newline='') as file:
			writer = csv.writer(file)
			writer.writerow(line[1:-1])
		




def parseEquation(eq):	

	eq = re.sub('[()]','',eq)	
	tokens = eq.split(',')
	formula = tokens[0]
	interest = tokens[1]
	year = int(tokens[2])

	filenm = '.\\data\\' + interest + '.csv'

	with open(filenm,'r') as file:
		linereader = csv.reader(file,delimiter=',')
		data = list(linereader)
		for i in range(len(data[1])):
			if formula in data[1][i]:				
				break
	
	return data[year+1][i]



def solveEquation(expr):
	expr = re.sub('[()]','',expr)   
	lis = expr.split(",")
	calc = lis[0][0].lower()
	using = lis[0][2].lower()
	n = int(lis[2])
	i = (float(lis[1]))/100.0
	result = 0.0
	if(calc == 'p' and using == 'f'):
		result = 1.0/((1.0+(i))**n)
	elif(calc == 'p' and using == 'a'):
		temp = (1.0 + i)**n
		result = (temp-1)/(i * temp)
	elif(calc == 'p' and using == 'g'):
		s = 1.0+i
		k = 1.0/s
		result = (k**2-k**(n+1))/((1-k)**2) - (n-1) * k**(n+1)/(1-k)
	elif (calc == 'f' and using == 'p'):
		result = (1.0+i)**n
	elif(calc == 'f' and using == 'a'):
		result = ((1.0 + i)**n - 1)/i
	elif (calc == 'a' and using == 'p'):
		temp = (1.0 + i)**n
		result = (i*temp)/(temp-1)
	elif (calc == 'a' and using == 'f'):
		result = i/((1.0 + i)**n - 1)
	elif (calc == 'a' and using == 'g'):
		s = 1.0+i
		k = 1.0/s
		temp1 = (k**2-k**(n+1))/((1-k)**2) - (n-1) * k**(n+1)/(1-k)
		temp = (1.0 + i)**n
		result = ((i*temp)/(temp-1)) * temp1
	if (calc == 'a' and using == 'f') or (calc == 'f' and using == 'a') or (calc == 'a'and using == 'p'):
		result = round(result, 5)
	else:
		result = round(result, 4)	
	return str(result)



def checkInterest(eq):
	eq = re.sub('[()]','',eq)	
	tokens = eq.split(',')
	interest = tokens[1]
	return (interest in interests)




def main():
	eq = input('Enter equation: ')
	#eq = '10*(F/P,10.0,5) + 5*(F/A,10.0,5) - (F/A,10.0,5)'
	eq = eq.replace(' ','')
	tokens = re.split('([*+-])',eq)	
	for token in tokens:
		print(token,end=' ')
	print()

	for i in range(len(tokens)):
		if tokens[i][0]=='(':			
			check = checkInterest(tokens[i])
			if check==True:
				tokens[i] = parseEquation(tokens[i])					
			else:
				tokens[i] = solveEquation(tokens[i])


	final_str = " ".join(tokens)
	print(final_str)	
	code = parser.expr(final_str).compile()
	print(eval(code))


if __name__=='__main__':
	main()

	#cleanFile()
	#createFiles()	
	#populateFiles()