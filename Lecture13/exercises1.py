#!bin/python3
seq=open('input.txt')
output=open('output_clean.txt','w')
for line in seq:
	seq_clean=line[14:]
	print(seq_clean)
	output.write(seq_clean+'\n')
seq.closed
output.closed
