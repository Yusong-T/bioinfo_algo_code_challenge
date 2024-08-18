from collections import defaultdict

def DeBruijn(text):
    k = int(text[0])
    l = k - 1
    string = text[1]
    collection_1 = {}
    for i in range(len(string)-l+1):
        collection_1[i] = string[i:i+l]
    # print(collection)
    collection_2 = {}
    for i in range(len(string)-l):              # removes the last kmer for candidates on the left side of the colon
        collection_2[i] = string[i:i+l]
    d = defaultdict(list)
    for key,value in collection_2.items():
        d[value].append(collection_1[key+1])
    # print(d)
    for key,value in d.items():
        mod_result = " ".join(value)
        with open('result.txt','a+') as fh:
            print("%s: %s"%(key,mod_result),file = fh)

text = open('dataset_199_6.txt').read().split()

DeBruijn(text)
