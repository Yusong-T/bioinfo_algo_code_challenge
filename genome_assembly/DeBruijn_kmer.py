from collections import defaultdict

def DeBruijn_kmer(text):
    k = len(text[0])
    l = k - 1
    d = defaultdict(list)
    for pattern in text:
        d[pattern[:l]].append(pattern[1:])
    for key,value in d.items():
        mod_result = " ".join(value)
        with open('result.txt','a+') as fh:
            print("%s: %s"%(key,mod_result), file = fh)



text = open('dataset_200_8.txt').read().split()

DeBruijn_kmer(text)
