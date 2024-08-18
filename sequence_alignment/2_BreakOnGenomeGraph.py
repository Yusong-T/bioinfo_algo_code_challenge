def BreakOnGenomeGraph(GenomeGraph, indices):
    try:
        GenomeGraph.remove([indices[0], indices[1]])
    except:
        GenomeGraph.remove([indices[1], indices[0]])
    try:
        GenomeGraph.remove([indices[2], indices[3]])
    except:
        GenomeGraph.remove([indices[3], indices[2]])
    GenomeGraph.append([indices[0], indices[2]])
    GenomeGraph.append([indices[1], indices[3]])
    return GenomeGraph


text = open('dataset_8224_2.txt').read().split('\n')
graph = text[0]
indices = text[1]
graph = graph.split('), (')
graph[0] = graph[0].replace("(","")
graph[-1] = graph[-1].replace(")","")
genome_graph = []
for group in graph:
    group = group.split(', ')
    group = [int(x) for x in group]
    genome_graph.append(group)
indices = indices.split(', ')
indices = [int(x) for x in indices]
results = BreakOnGenomeGraph(genome_graph, indices)
with open('out.txt', 'w') as fh:
    print(results, file = fh)
output = open('out.txt').read()
output = output[1:-2]
output = output.replace("[","(")
output = output.replace("]",")")
print(output)
