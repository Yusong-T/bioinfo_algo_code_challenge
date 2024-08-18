import math
from collections import defaultdict
import random

# another way to generate binary combinations:
# from itertools import product
def Kmercollection(k):
    kmers = []
    for i in range(int(math.pow(2,k))):
        kmer = f'{i:08b}'                            # !!! manually append the number of 0s before use
        kmers.append(kmer)
    return kmers

def DeBruijn_kmer(text):
    k = len(text[0])
    l = k - 1
    d = defaultdict(list)
    for pattern in text:
        d[pattern[:l]].append(pattern[1:])
    for key,value in d.items():
        mod_result = " ".join(value)
        with open('result_1.txt','a+') as fh:
            print("%s: %s"%(key,mod_result), file = fh)

def Directory(raw_data):
    d = defaultdict(list)
    for line in raw_data:
        temp = line.split(':')
        former = temp[0]
        temp_2 = temp[1].split(' ')
        for i in range(1,len(temp_2)):
            d[former].append(temp_2[i])
    return d

def EulerianCycle(d):
    stat = defaultdict(list)
    fnode = []
    for key in d.keys():
        stat[key].append(len(d[key]))                   # counts the out-degree
        fnode.append(key)
    for node in fnode:                                  # counts the in-degree
        count = 0
        for value in d.values():
            for num in value:
                if num == node:
                    count += 1
        stat[node].append(count)
#    print(stat)
    vertex = None
    for key in stat.keys():
        if stat[key][0] > stat[key][1]:
            vertex = key
    if vertex == None:
        vertex = random.choice(fnode)
    stack = []
    circuit = []
    while True:
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
    circuit.append(circuit[0])
    with open('result_2.txt','a+') as fh:
        print(*circuit, file = fh)

def GenomePath(path):
    l = len(path[0])
    string = list(path[0])
    for substr in path[1:]:
        string.append(substr[l-1])
    gstring = "".join(string)
    print(gstring)
    result = gstring[:int(math.pow(2,k))]
    return result


k = 8
DeBruijn_kmer(Kmercollection(k))
raw_data = open('result_1.txt').read().splitlines()
EulerianCycle(Directory(raw_data))
path = open('result_2.txt').read().split()
fh = open('result.txt','a+')
print(GenomePath(path), file = fh)
fh.close()
