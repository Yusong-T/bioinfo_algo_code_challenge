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
def rdna(pattern):
    pattern_r = []
    for tide in pattern:
    	if tide == 'A':
    		pattern_r.append('T')
    	elif tide =='T':
    		pattern_r.append('A')
    	elif tide == 'C':
    		pattern_r.append('G')
    	elif tide == 'G':
    		pattern_r.append('C')
    pattern_r.reverse()
    return ''.join(pattern_r)                       # converts list to str

def FrequentWordsWithMismatches(text,k,d):
    freqmap = {}
    patterns = []
    tmap = {}
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        neighborhood = neighbors(pattern,d)
        for neighbor in neighborhood:
            neighbor_r = rdna(neighbor)
            freqmap[neighbor] = freqmap.get(neighbor,0) + 1
            freqmap[neighbor_r] = freqmap.get(neighbor_r,0) + 1
            tmap[neighbor] = freqmap[neighbor] + freqmap[neighbor_r]
    m = max(tmap.values())
    for key in tmap:
        if tmap[key] == m:
            patterns.append(key)
            patterns.append(rdna(key))
    return patterns

text = 'TGATATGGTTGTGCTGTGCGTGTCGTGCTGCCGCGCGTGCGTTGTGTGCCGTGCATACGTGATATGGTTGCATAATACGTGCGTGCGTTGTGCTGGTATATGCATAATATGTGCTGCATATGCCGGTTGGTGTCGCGTGCGTGTATATGTGCTGTGCCGTGGTATAGTTGCTGCATATGCATATGCATATGTGCATATGATACGATATGCATATGTG'
k = 6
d = 2

print(*FrequentWordsWithMismatches(text,k,d))
