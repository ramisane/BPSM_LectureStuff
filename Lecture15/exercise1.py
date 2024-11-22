#!bin/python3
def get_aa_percentage(protein,aa='LMF'):
  aa_count=0
  for aa_base in aa:
    aa_count = aa_count + protein.upper().count(aa_base.upper())
  aa_content = round(aa_count*100/len(protein))
  return(aa_content)

assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP") == 65
