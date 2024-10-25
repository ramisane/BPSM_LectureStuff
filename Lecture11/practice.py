#!/usr/bin/python3
seq="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
length=len(seq)
count_a=seq.count('A')
count_t=seq.count('T')
print("length:" + str(length))
print("a:" + str(count_a))
print("t:" + str(count_t))
print("a&t:" + str((count_a+count_t)/length))
complement={'A':'T','T':'A','C':'G','G':'C'}
print(complement[str(seq)])
