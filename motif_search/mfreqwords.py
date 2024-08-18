# find the most frequent words with at most d mismatches

def hammingdis(p,q):
    count = []
    for i in range(0,len(p)):
        if p[i] == q[i]:
            continue
        else:
            count.append(i)
    return len(count)

def neighbors(pattern,d):                               # returns the neighborhood of pattern
    if d == 0:
        return pattern
    elif len(pattern) == 1:
        return ['A','C','T','G']
    else:
        neighborhood = []
        suffixneighbors = neighbors(pattern[1:],d)      # recursion
        for text in suffixneighbors:
            if hammingdis(pattern[1:],text) < d:
                for x in ['A','T','C','G']:
                    neighborhood.append(x + text)
            else:
                neighborhood.append(pattern[0] + text)
    return neighborhood

# pattern = 'AACGCCGTAC'
# d = 3
# print(*neighbors(pattern,d))

def FrequentWordsWithMismatches(text,k,d):
    freqmap = {}
    patterns = []
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        neighborhood = neighbors(pattern,d)
        for neighbor in neighborhood:
            freqmap[neighbor] = freqmap.get(neighbor,0) + 1
    m = max(freqmap.values())
    for key in freqmap:
        if freqmap[key] == m:
            patterns.append(key)
    return patterns

text = 'CTTCAATGAGCTTCCTTCCTTCAATCAATCAATCAATCTTCTTGAGCAATGAGGTGCTTGTGGTGCTTCAATGAGGAGCAATGTGCAATGTGCAATCAATCTTCCTTCTTCGAGCAATCTTCCTTGAGCAATGAGCTTCTTGAGGAGGAGCAATCTTCTTCGAGCTTGTGGAGGTGGAGCTTCCTTCAATGAGGAGGTGGTGGTGCTTCCTTGAGCTTCCTTCCTTGTGCTTCTTCCTTCCTTCTTCCTTGTGCAATCTTCAATCTTCTTCCAATGAGCTTCTTCCTTCTTGAGCTTCTTCGTGGTGCTTGTGCAATGAGGTGCAATCTTCTTCGTGCAATCTTCTTCAATGTGGTGGTGGTGGTGCTTGTGCAATCAATGTGGAG'
k = 6
d = 2

result_1 = FrequentWordsWithMismatches(text,k,d)

# result_2 = []
# for i in result_1:
#     for tide in i:
#         c_dna = []
#         if tide == 'A':
#             c_dna.append('T')
#         elif tide =='T':
#             c_dna.append('A')
#         elif tide == 'C':
#             c_dna.append('G')
#         elif tide == 'G':
#             c_dna.append('C')
#     result_2.append(c_dna.reverse())


result = result_1 #+ result_2
print(*result)
