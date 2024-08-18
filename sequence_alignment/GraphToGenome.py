def CycleToChromosome(nodes):
    chromosome = []
    for i in range(int(len(nodes)/2)):
        if nodes[2*i] < nodes[2*i+1]:
            chromosome.append(int((min(nodes)+1)/2)+i)
        else:
            chromosome.append(-(int((min(nodes)+1)/2)+i))
    return chromosome

def GraphToGenome(graph):
    collections = []
    chromosomes = []
    nodes = []
    for edge in graph:
        if edge[0] > edge[1]:
            nodes.append(edge[0])
            nodes.insert(0, edge[1])
            chromosomes.append(nodes)
            nodes = []
            continue
        nodes.append(edge[0])
        nodes.append(edge[1])
    for chromosome in chromosomes:
        collections.append(CycleToChromosome(chromosome))
    return collections

text = open('dataset_8222_8.txt').read().split('), (')
text[0] = text[0].replace("(","")
text[-1] = text[-1].replace(")","")
cycle = []
for group in text:
    group = group.split(', ')
    group = [int(x) for x in group]
    cycle.append(group)
results = GraphToGenome(cycle)
for result in results:
    for i in range(len(result)):
        if result[i] > 0:
            result[i] = '+' + str(result[i])
    print('(', end = '')
    print(*result, end = '')
    print(')', end = '')
