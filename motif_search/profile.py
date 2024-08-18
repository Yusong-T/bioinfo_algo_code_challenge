text = '''TGTGTCTTTGAGTATTTTTACCAGCCATGCTCTGGCTATCCCAAACGGTTGCTGTGATTCCGAACCCCAGTAAGATGAGATATTTATCCGACACGTGCTTCAATGCGTTCTTAACCCCGAAAAAACTGGTGACGAGTAAGCATTGATGGCGCACTCAATAATGGCCGGTGTTCGCTCAACTTCCAAACGTAGGGGATTGAAATTCGCACGATCTACGGGCCAGACAATACCTTACATTAACTCGCGGGATGTCACTAGGTAGTTGAGCCCAATTGGCGGTGGTACGCCGATACCCGTTGCCTTCTGCCACTTCGGCGGAGCCTATCGCGCGAGGGTATTGGCTCTCGGTCCCGTAGCGGATAGACACTCAAACGCGAGTCCTTACCCTATGGTTCTCAAAGAAGAGGAGGCACCGGCACGTACCCGGTATTCGAAGGAGCAGGAAAGCGATGGTTAACGTGGGTCCAAAACTGAACACCATATCGAGGTTTGTGTAGAGACGTGATGCTCCGATGTTCTGGATGGTCCGTTCACCATCCGAATATTCTATACCCAGTCAAGGACACTTGCTCCACCCTAAAGCAAGATAATGGTAGTGACCGACCTCTCCCCCATGTGTGACCGCGTCAGATCTTAGGGTCACTAAAACATCCGATACGGCAGCACCTTCCCCGAAAAACGCTCATCGACAGCGTCGAGGCGGGGATATGTCCGGCTTCATCCAACCAGATCAGTGCCGCAAACGGGGTGGTCCCACAACGCGTGAGCCCAACGCTTTAATGCCGATATTACTCTCTATTCATAGCGTAGTAGCCGGAGTTTAAAACCGCACAGAGCAAAGGACTCGCTTTCCCAAGATTTAAATGAAGGGTTCTCAAACTATTGTCCGTCCACTTGAGTGTTGAGCCACCGCTTTTTTTGAGCGGAGCTTGTTGCTAGTCTGTACAGCCCCCTACCTCCTATTAGGCTGAGAGCGAACCGCATGGAGCTGACCAGCATA'''
d = 12

with open('matrix.txt') as file_object:
    lines = file_object.readlines()
pro_string = ''
for line in lines:
    pro_string = pro_string + ' ' + line.rstrip()
# print(pro_string)
# print(pro_string[1:4])
score = 0
for i in range(len(text)-d+1):
    prob = 1
    for j in range(d):
        if text[i+j] == 'A':
            prob *= float(pro_string[1+6*j:6+6*j])
        elif text[i+j] == 'C':
            prob *= float(pro_string[6*d+1+6*j:6*d+6+6*j])
        elif text[i+j] == 'G':
            prob *= float(pro_string[12*d+1+6*j:12*d+6+6*j])
        elif text[i+j] == 'T':
            prob *= float(pro_string[18*d+1+6*j:18*d+6+6*j])
    if prob > score:
        score = prob
        position = i

print(text[position:position+d])



# other's solution

# with open('E:\FILES\BioinfStud\Coursera\dataset_4_5.txt', 'r') as file:
# 	Text = file.readline().strip()
# 	k = int(file.readline().strip())
# 	Nuc_prob = {}
# 	Nuc_prob['A'] = file.readline().strip().split(' ')
# 	Nuc_prob['C'] = file.readline().strip().split(' ')
# 	Nuc_prob['G'] = file.readline().strip().split(' ')
# 	Nuc_prob['T'] = file.readline().strip().split(' ')
#
#
# def MostProPat(Text, k, Nuc_prob):
# 	Prob = 0
# 	for i in range(len(Text) - k):
# 		prob = 1
# 		k_mer = Text[i: i + k]
# 		for nuc in range(k):		#0,1,2,3,4
# 			for Nuc in Nuc_prob:	#ATGC
# 				if k_mer[nuc] == Nuc:
# 					prob *= float(Nuc_prob[Nuc][nuc])
# 		if prob > Prob:
# 			Prob = prob
# 			answ = k_mer
# 	return(answ)

# print(MostProPat(Text, k, Nuc_prob))
