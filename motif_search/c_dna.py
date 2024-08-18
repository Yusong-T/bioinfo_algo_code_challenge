dna = 'GCTAGCT'
c_dna = []
for tide in dna:
	if tide == 'A':
		c_dna.append('T')
	elif tide =='T':
		c_dna.append('A')
	elif tide == 'C':
		c_dna.append('G')
	elif tide == 'G':
		c_dna.append('C')
c_dna.reverse()

print (*c_dna)




# # Other solutions_1
# def ReverseComplement(pattern:str):
#     trans = str.maketrans('ATCG', 'TAGC')
#     return pattern.translate(trans)[::-1]

# with open(r'dataset_3_2.txt') as f:
#     pattern = f.readline().strip()
#     print(ReverseComplement(pattern))




# # Other solutions_2
# def ReverseComp():
#   dnapatt = input("Enter Sequence:")
#   reversecomp = ''
#   for base in dnapatt:
#     if base == "A":
#       reversecomp += "T"
#     elif base == "T":
#       reversecomp += "A"
#     elif base == "G":
#       reversecomp += "C"
#     elif base == "C":
#       reversecomp += "G"

#   return reversecomp[::-1]
