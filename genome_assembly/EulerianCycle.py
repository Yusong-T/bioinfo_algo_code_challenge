from collections import defaultdict
import random

def Directory(raw_data):
    d = defaultdict(list)
    for line in raw_data:
        temp = line.split(':')
        former = temp[0]
        temp_2 = temp[1].split(' ')
        for i in range(1,len(temp_2)):
            d[former].append(temp_2[i])
    return d

# def EulerianCycle(d):
#     cycle = []
#     former = random.choice(list(d.keys()))
#     latter = random.choice(d[former])
#     cycle.append(former)
#     cycle.append(latter)
#     edge_count = 1
#     while True:                                     # randomly builds a cycle
#         former = latter
#         latter = random.choice(d[former])
#         flag = 0
#         for i in range(edge_count):
#             if cycle[i] == former and cycle[i+1] == latter:     # don't visit the same edge twice
#                 flag = 1
#         if flag == 1:
#             continue
#         cycle.append(latter)
#         edge_count += 1
#         if latter == cycle[0]:
#             break
#     edges = 0
#     for value in d.values():                        # counts the number of edges
#         edges += len(value)
#     while len(cycle) < edges+1:


# http://www.graph-magics.com/articles/euler.php

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
    with open('result.txt','a+') as fh:
        print(*circuit, file = fh)






#raw_data = open('dataset_203_2.txt').readlines()
raw_data = open('dataset_203_2.txt').read().splitlines()        # reads the file without '\n'
#print(Directory(raw_data))
EulerianCycle(Directory(raw_data))
