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

def MNBP(d):
    stat = defaultdict(list)
    nodes = [node for node in d.keys()]
    for key in nodes:
        stat[key].append(len(d[key]))
    for node in nodes:
        count = 0
        for value in d.values():
            for num in value:
                if num == node:
                    count += 1
                if num not in nodes:                         # counts the nodes without out-degree
                    stat[num].append(0)
        stat[node].append(count)
    paths = []
    for v in d.keys():
        if stat[v][0] != 1 or stat[v][1] != 1:
            try:
                nodes.remove(v)
            except:
                None
            for w in d[v]:
                path = []
                path.append(v)
                path.append(w)
                try:
                    nodes.remove(w)
                except:
                    None
                while stat[w][0] == 1 and stat[w][1] == 1:
                    path.append(d[w][0])
                    w = d[w][0]
                    try:
                        nodes.remove(w)
                    except:
                        None
                paths.append(path)
#    print(nodes)
    for startnode in nodes:
        # if startnode in paths[-1]:
        #     continue
        if stat[startnode][0] == 1 and stat[startnode][1] == 1:
            path = []
            path.append(startnode)
            i = d[startnode][0]
            while i != startnode:
                path.append(i)
                nodes.remove(i)                     # important: avoid overlapping paths (haven't figure it out why)
                i = d[i][0]
            path.append(i)
            paths.append(path)
    with open('result.txt', 'a+') as fh:
        for path in paths:
            print(*path, file = fh)






#raw_data = open('test.txt').read().splitlines()
raw_data = open('dataset_6207_2.txt').read().splitlines()
MNBP(Directory(raw_data))
