#!bin/python3
import matplotlib.pyplot as plt
import numpy as np
ecoli=open("ecoli.txt").read().replace('\n','').upper()
window=1000
regions=[50000,100000,len(ecoli)]
for region in regions:
  print("processing "+str(region))
  at_content=[]
  for start in range(region-window):
    win=ecoli[start:start+window]
    at_content.append((win.count("A")+win.count("T"))/window)
  plt.figure(figsize=(10,20))
  plt.plot(at_content,label="AT Content",linewidth=3)
  plt.ylabel("Fraction of bases")
  plt.xlabel("Position on genome")
  plt.title("AT content of 1kb windows of E.coli")
  plt.legend(loc="upper right")
  plt.savefig("Excersise1"+str(region)+".png",transparent=True)
  plt.show()
