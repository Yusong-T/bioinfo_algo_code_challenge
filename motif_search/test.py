dna = 'ATTTCG CCGGTA GGAATT AACGAT'
stan = ''
for tide in dna:
    if tide == ' ':
        break
    stan += tide
print(stan)
