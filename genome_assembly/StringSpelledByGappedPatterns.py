def GenomePath(path):
    k = len(path[0])
    string = list(path[0])
    for substr in path[1:]:
        string.append(substr[k-1])
    gstring = "".join(string)
    return gstring

def StringSpelledByGappedPatterns(GappedPatterns,k,d):
    FirstPatterns = []
    SecondPatterns = []
    for pattern in GappedPatterns:
        FirstPatterns.append(pattern[:k])
        SecondPatterns.append(pattern[k+1:])
    Prefixstring = GenomePath(FirstPatterns)
    Suffixstring = GenomePath(SecondPatterns)
    flag = 0
    for i in range(k+d,len(Prefixstring)):
        if Prefixstring[i] != Suffixstring[i-k-d]:
            flag = 1
            return 'there is no string spelled by the gapped patterns'
            break
    if flag == 0:
        genome = Prefixstring + Suffixstring[-(k+d):]
        return genome




text = open('test.txt').read().split()
#text = open('dataset_6206_4.txt').read().split()
print(StringSpelledByGappedPatterns(text,3,1))
