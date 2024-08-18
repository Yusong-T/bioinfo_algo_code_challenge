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

def MoEnum(dna,k,d):
    patterns = []
    reftext = ''
    for tide in dna:
        if tide == ' ':
            break
        reftext += tide
    n = len(reftext)
    num = (len(dna)+1)/(n+1)
    for i in range(0,n-k+1):
        ipattern = reftext[i:i+k]
        for pattern in neighbors(ipattern,d):
            count = 0
            for w in range(n+1,len(dna)-n+1,n+1):
                for m in range(w,w+n-k+1):
                    qpattern = dna[m:m+k]
                    if hammingdis(qpattern,pattern) <= d:
                        count += 1
                        break
            if count == num - 1:
                patterns.append(pattern)
    return patterns

k = 5
d = 2
dna = 'GGCCCCTGCAACGCCGGAGCCTCTT ACGTGACGCAATCCGGAACGAACCG TCTGAGACCTATAATCCGCTTCCTC GTCTTGCGATCGTGTGACATCCGCC AGACAGGCCCGTACCTGCTTACGCT GGCCCCCCAGCCGCGGCGGTGATAG'

print(*set(MoEnum(dna,k,d)))
