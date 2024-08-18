def OverLap(patterns):
    k = len(patterns[0])
    n = len(patterns)
    for i in range(n):
        poped = patterns.pop(i)
        pattern_list = []
        flag = 0
        for pattern in patterns:
            if poped[1:] == pattern[:k-1]:
                pattern_list.append(pattern)
                flag += 1
        if flag > 0:
            mod_pat = ' '.join(pattern_list)
            with open('result.txt','a+') as fh:
                print("%s: %s"%(poped,mod_pat), file = fh)
        patterns.insert(i,poped)

patterns = open('dataset_198_10.txt').read().split()
#print(patterns)
# fh = open('result.txt','a+')
# print(OverLap(patterns), file = fh)
# fh.close()
OverLap(patterns)
