#!/bin/bash
for originfile in  /home/s2542650/Exercises/fastq/*.fq.gz
do fastqc ${originfile} -o /home/s2542650/Exercises/fastq/outputtest
	for fqfile in /home/s2542650/Exercises/fastq/outputtest/*.zip
	do unzip ${fqfile} ${originfile}/summary.txt | awk 'BEGIN{FS="\t"}{NR=1}
		{
		if($1== "PASS")
		echo "$2" >> /home/s2542650/Exercises/fastq/outputtest/pass.list 
		}'
	done
done
