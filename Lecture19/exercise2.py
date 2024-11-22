#!bin/python3
import matplotlib.pyplot as plt
import numpy as np
def getcontentfig(window,content,startpos,endpos):
  ecoli=open("ecoli.txt").read().replace('\n','').upper()
  content=[]
  windowamount=int(endpos)-int(startpos)-int(window)
  for start in range(windowamount):
    win=ecoli[int(startpos)+start:int(startpos)+start+int(window)]
    if content == "AT":
      content.append((win.count("A")+win.count("T"))/window)
    elif content == "GC":
      content.append((win.count("G")+win.count("C"))/window)
  plt.figure(figsize=(10,20))
  plt.plot(at_content,label="Content",linewidth=3)
  plt.ylabel("Fraction of bases")
  plt.xlabel("Position on genome")
  plt.title("AT content of 1kb windows of E.coli")
  plt.legend(loc="upper right")
  plt.savefig("Excersise2"+str(region)+".png",transparent=True)
  plt.show()
  print("Figure saved")

window=input("please input the window size:")
content=input("please choose AT or GC:")
startpos=input("please input the starposition:")
endpos=input("please input the end position:")
getcontentfig(window,content,startpos,endpos)
