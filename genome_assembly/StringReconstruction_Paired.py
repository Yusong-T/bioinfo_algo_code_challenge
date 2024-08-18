# simplify the codes as much as possible!!!

from collections import defaultdict
import random

def DeBruijn_kmer_paired(text):
    l = k - 1
    d = defaultdict(list)
    for pattern in text:
        prefix = "".join([pattern[:l],pattern[k:k+l+1]])
        suffix = "".join([pattern[1:k+1],pattern[-l:]])
        d[prefix].append(suffix)
    return d

def EulerianPath(d):
    stat = defaultdict(list)
    lnode = []
    for key in d.keys():
        stat[key].append(len(d[key]))                      # counts the out-degree
    for node in d.keys():                                  # counts the in-degree
        count = 0
        for value in d.values():
            for num in value:
                lnode.append(num)
                if num == node:
                    count += 1
        stat[node].append(count)
    endnode = None
    for node in lnode:
        if node not in d.keys() or stat[node][1] - stat[node][0] == 1:
            endnode = node
    vertex = None
    for key in stat.keys():
        if stat[key][0] - stat[key][1] == 1:
            vertex = key
    d[endnode].append(vertex)                       # adds an edge from end to start
    stack = []
    circuit = []
    while 1:
        if len(d[vertex]) > 0:
            stack.append(vertex)
            chosen = random.choice(d[vertex])
            d[vertex].remove(chosen)
            vertex = chosen
        else:
            circuit.append(vertex)
            last_vertex = stack.pop()
            vertex = last_vertex
        if len(d[vertex])==0 and len(stack)==0:
            break
    circuit.reverse()
#    circuit.append(circuit[0])
    for i in range(len(circuit)):
        if circuit[i] == endnode:
            index = i
    str_1 = circuit[index+1:]
    str_2 = circuit[:index+1]
    str = str_1 + str_2
    return str
    # print(str)
    # with open('result_2.txt','a+') as fh:
    #     print(*str, file = fh)

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
        FirstPatterns.append(pattern[:k-1])
        SecondPatterns.append(pattern[k:])
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


content = open('test.txt').read().split()
#content = open('dataset_204_16.txt').read().split()
k = int(content[0])
d = int(content[1])
text = content[2:]
# DeBruijn_kmer_paired(text)
# raw_data = open('result_1.txt').read().splitlines()
#print(Directory(raw_data))
gappedpatterns = EulerianPath(DeBruijn_kmer_paired(text))
#gappedpatterns = open('result_2.txt').read().split()
with open('result.txt','a+') as fh:
    print(StringSpelledByGappedPatterns(gappedpatterns,k,d), file = fh)
