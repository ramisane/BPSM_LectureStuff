#!bin/python3
data=open('data.csv').read().rstrip().split('\n')
#print(data)
for line in data:
	linelist=line.split(',')
	#
	if linelist[0]=="Drosophila melanogaster" or linelist[0]=="Drosophila simulans":
		print(linelist[2])



