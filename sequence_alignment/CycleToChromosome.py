def CycleToChromosome(nodes):
    chromosome = []
    for i in range(int(len(nodes)/2)):
        if nodes[2*i] < nodes[2*i+1]:
            chromosome.append(i+1)
        else:
            chromosome.append(-(i+1))
    return chromosome






text = open('dataset_8222_5.txt').read().strip("(").strip(")").split()
text[len(text)-1] = text[len(text)-1].replace(")","")                   # remove the ')' at the end
text = [int(x) for x in text]
result = CycleToChromosome(text)
for i in range(len(result)):
    if result[i] > 0:
        result[i] = '+' + str(result[i])
print('(', end = '')
print(*result, end = '')
print(')')
