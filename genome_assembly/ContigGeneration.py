from collections import defaultdict

def DeBruijn_kmer(text):
    k = len(text[0])
    l = k - 1
    d = defaultdict(list)
    for pattern in text:
        d[pattern[:l]].append(pattern[1:])
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
        stat[node].append(count)
#    print(stat)
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
                try:
                    while stat[w][0] == 1 and stat[w][1] == 1:
                        path.append(d[w][0])
                        w = d[w][0]
                        try:
                            nodes.remove(w)
                        except:
                            None
                except:
                    None
                paths.append(path)
##    print(nodes)
    for startnode in nodes:
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
    return paths

def GenomePath(path):
    k = len(path[0])
    string = list(path[0])
    for substr in path[1:]:
        string.append(substr[k-1])
    gstring = "".join(string)
    return gstring


text = open('dataset_205_5.txt').read().split()
paths = MNBP(DeBruijn_kmer(text))
result = []
for path in paths:
    result.append(GenomePath(path))
with open('result.txt', 'a+') as fh:
    print(*result, file = fh)
