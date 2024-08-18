# remember to clear all content of result_1 and result_2 !!!

from collections import defaultdict
import random

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

def EulerianPath(d):
    stat = defaultdict(list)
    fnode = []
    lnode = []
    for key in d.keys():
        stat[key].append(len(d[key]))                   # counts the out-degree
        fnode.append(key)
    for node in fnode:                                  # counts the in-degree
        count = 0
        for value in d.values():
            for num in value:
                lnode.append(num)
                if num == node:
                    count += 1
        stat[node].append(count)
    endnode = None
    for node in lnode:
        if node not in fnode:
            endnode = node
        elif stat[node][1] - stat[node][0] == 1:
            endnode = node
    #print(endnode)
    # stat[endnode].append(0)
    # stat[endnode].append(1)
    #print(stat)
    #print(endnode)
    vertex = None
    for key in stat.keys():
        if stat[key][0] - stat[key][1] == 1:
            vertex = key
    d[endnode].append(vertex)                       # adds an edge from end to start
    #print(d)
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
#    circuit.append(circuit[0])
    for i in range(len(circuit)):
        if circuit[i] == endnode:
            index = i
    str_1 = circuit[index+1:]
    str_2 = circuit[:index+1]
    str = str_1 + str_2
    with open('result_2.txt','a+') as fh:
        print(*str, file = fh)

def GenomePath(path):
    k = len(path[0])
    string = list(path[0])
    for substr in path[1:]:
        string.append(substr[k-1])
    gstring = "".join(string)
    return gstring



text = open('dataset_203_7.txt').read().split()
DeBruijn_kmer(text)
raw_data = open('result_1.txt').read().splitlines()
EulerianPath(Directory(raw_data))
path = open('result_2.txt').read().split()
fh = open('result.txt','a+')
print(GenomePath(path), file = fh)
fh.close()
