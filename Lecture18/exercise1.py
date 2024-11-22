#!bin/python3
import re
accessions = [
  'xkn59438', 
  'yhdck2', 
  'eihd39d9', 
  'chdsye847', 
  'hedle3455', 
  'xjhd53e', 
  '45da', 
  'de37dp']
for acc in accessions:
 re.research(r'5',acc)
 re.research(r'[de]',acc)
 re.research(r'de',acc)
 re.research(r'd{1,1}e',acc)
 re.research(r'd',acc) and re.research(r'e',acc)
 re.research(r'^[xy]',acc)
 re.research(r'^[xy]',acc) and re.research(r'e$',acc)
 re.research(
