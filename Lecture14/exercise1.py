#!bin/python3
data=open('data.csv').read().rstrip().split('\n')
#print(data)
for line in data:
	linelist=line.split(',')
	at_amount=(linelist[1].count("a")+linelist[1].count("t"))/len(linelist[1])
	if linelist[0]=="Drosophila melanogaster" or linelist[0]=="Drosophila simulans":
		print("1.:"+linelist[2])
	if len(linelist[1])>90 and len(linelist[1])<100:
		print("2.:"+linelist[2])
	if at_amount<0.5 and int(linelist[3])>200:
		print("3.:"+linelist[2])
	if linelist[2].startswith("k") or linelist[2].startswith("h") and linelist[0]!="Drosophila melanogaster":
		print("4.:"+linelist[2])
	if at_amount > 0.65:
		print("5.:"+linelist[2]+" high")
	elif at_amount < 0.45:
		print("5.:"+linelist[2]+" low")
	else:
		print("5.:"+linelist[2]+" medium")
