def GenomePath(path):
    k = len(path[0])
    string = list(path[0])
    for substr in path[1:]:
        string.append(substr[k-1])
    gstring = "".join(string)
    return gstring

path = open('dataset_198_3.txt').read().split()
print(path)
fh = open('result.txt','a+')
print(GenomePath(path), file = fh)
fh.close()
