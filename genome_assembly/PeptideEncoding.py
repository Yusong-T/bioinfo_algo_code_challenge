
# GeneticCode = {"TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L",
#     "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S",
#     "TAT":"Y", "TAC":"Y", "TAA":"", "TAG":"",
#     "TGT":"C", "TGC":"C", "TGA":"", "TGG":"W",
#     "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
#     "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
#     "CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
#     "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R",
#     "ATT":"I", "ATC":"I", "ATA":"I", "ATG":"M",
#     "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
#     "AAT":"N", "AAC":"N", "AAA":"K", "AAG":"K",
#     "AGT":"S", "AGC":"S", "AGA":"R", "AGG":"R",
#     "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
#     "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
#     "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E",
#     "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G"}

codon_table = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"*", "UAG":"*",
    "UGU":"C", "UGC":"C", "UGA":"*", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}

def reversecomp(Dna):
    c_dna = []
    for tide in Dna:
    	if tide == 'A':
    		c_dna.append('T')
    	elif tide =='T':
    		c_dna.append('A')
    	elif tide == 'C':
    		c_dna.append('G')
    	elif tide == 'G':
    		c_dna.append('C')
    c_dna.reverse()
    c_dna = "".join(c_dna)
    return c_dna

def transcription(Dna):
    rna = []
    for tide in Dna:
    	if tide == 'A':
    		rna.append('A')
    	elif tide =='T':
    		rna.append('U')
    	elif tide == 'C':
    		rna.append('C')
    	elif tide == 'G':
    		rna.append('G')
    rna = "".join(rna)
    return rna

def ProteinTranslation_readingframe(rna,codon_table):
    l = len(rna)
    peptide_collection = []
    aa_string = []
    for i in range(0,l-2,3):
        aa_string.append(codon_table[rna[i:i+3]])
    aa_string = "".join(aa_string)
    peptide_collection.append(aa_string)
    aa_string = []
    for i in range(1,l-4,3):
        aa_string.append(codon_table[rna[i:i+3]])
    aa_string = "".join(aa_string)
    peptide_collection.append(aa_string)
    aa_string = []
    for i in range(2,l-3,3):
        aa_string.append(codon_table[rna[i:i+3]])
    aa_string = "".join(aa_string)
    peptide_collection.append(aa_string)
    return peptide_collection

def PeptideEncoding(Dna, Peptide, GeneticCode):
    l = len(Dna)
    k = len(Peptide)
    reverse_Dna = reversecomp(Dna)
    Rna = transcription(Dna)
    reverse_Rna = transcription(reverse_Dna)
    Protein = ProteinTranslation_readingframe(Rna, codon_table)
    reverse_Protein = ProteinTranslation_readingframe(reverse_Rna, codon_table)
    substrings = []
    index = 0
    for peptide in Protein:
        for i in range(len(peptide)-k+1):
            if peptide[i:i+k] == Peptide:
                substrings.append(Dna[index+3*i:index+3*i+3*k])
        index += 1
    index = 0
    for peptide in reverse_Protein:
        for i in range(len(peptide)-k+1):
            if peptide[i:i+k] == Peptide:
                substrings.append(reversecomp(reverse_Dna[index+3*i:index+3*i+3*k]))
        index += 1
    print(len(substrings))
    return substrings



text = open('dataset_96_7.txt').read().split()
Dna = text[0]
Peptide = text[1]
# with open('test.txt','r') as file:
#     text = ""
#     for readline in file:
#         line = readline.strip()
#         text += line
# Peptide = 'VKLFPWFNQY'
# Dna = text
substrings = PeptideEncoding(Dna, Peptide, codon_table)
with open('result.txt', 'a+') as fh:
    for substring in substrings:
        print(substring, file = fh)
