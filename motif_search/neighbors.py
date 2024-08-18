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

pattern = 'CCAGTCAATG'
d = 1
print(len(neighbors(pattern,d)))
print(neighbors(pattern,d))
