import random

def ChromosomeToCycle(text):
    nodes = []
    for i in range(len(text)):
        if text[i] > 0:
            nodes.append(2*text[i]-1)
            nodes.append(2*text[i])
        else:
            nodes.append(2*(-text[i]))
            nodes.append(2*(-text[i])-1)
    return nodes

def ColoredEdges(groups):
    collections = []
    for group in groups:
        cycle = ChromosomeToCycle(group)
        cycle.append(cycle[0])
        for i in range(1,len(cycle),2):
            collections.append((cycle[i], cycle[i+1]))
    return collections

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

def CycleToChromosome(nodes):
    chromosome = []
    for i in range(0,len(nodes),2):
        if nodes[i] < nodes[i+1]:
            chromosome.append(int(nodes[i+1]/2))
        else:
            chromosome.append(-(int(nodes[i]/2)))
    return chromosome

def ChromosomeToCycle(chromosome):
    nodes_cycle = []
    if type(chromosome[0]) == list:
        for text in chromosome:
            nodes = []
            for i in range(len(text)):
                if text[i] > 0:
                    nodes.append(2*text[i]-1)
                    nodes.append(2*text[i])
                else:
                    nodes.append(2*(-text[i]))
                    nodes.append(2*(-text[i])-1)
            nodes_cycle.append(nodes)
    else:
        for i in range(len(chromosome)):
            if chromosome[i] > 0:
                nodes_cycle.append(2*chromosome[i]-1)
                nodes_cycle.append(2*chromosome[i])
            else:
                nodes_cycle.append(2*(-chromosome[i]))
                nodes_cycle.append(2*(-chromosome[i])-1)
    return nodes_cycle

def overlap(f_edge, l_edge):
    if f_edge[0]==l_edge[0] or f_edge[0]==l_edge[1] or f_edge[1]==l_edge[0] or f_edge[1]==l_edge[1]:
        return 1
    else:
        return 0

def Cycles(edges, blackedges):
#    print(edges)
#    print(blackedges)
    cycles = []
    while len(blackedges) != 0:
        cycle = []
        start_edge = random.choice(blackedges)
        cycle.append(start_edge)
        edges.remove(start_edge)
        blackedges.remove(start_edge)
#        print(blackedges)
        edge_1 = start_edge
        flag = 0
        while flag != 1:
            for edge in edges:
#                print(edge)
                if edge in blackedges:
                    if edge[0] == edge_1[1]:
                        cycle.append(edge)
                        edge_1 = edge
                        edges.remove(edge)
                        blackedges.remove(edge)
                    elif edge[1] == edge_1[1]:
                        cycle.append([edge[1], edge[0]])
                        edge_1 = [edge[1], edge[0]]
                        edges.remove(edge)
                        blackedges.remove(edge)
                else:
                    if edge_1[1] == edge[0]:
                        cycle.append(edge)
                        edge_1 = edge
                        edges.remove(edge)
                        if edge[1] == start_edge[0]:
                            flag = 1
                            break
                    elif edge_1[1] == edge[1]:
                        cycle.append([edge[1], edge[0]])
                        edge_1 = [edge[1], edge[0]]
                        edges.remove(edge)
                        if edge[0] == start_edge[0]:
                            flag = 1
                            break
        cycles.append(cycle)
#        print(cycle)
    return cycles

def BreakOnGenome(P, indices):
#    print(P)
    Edges = ChromosomeToCycle(P)
#    print(Edges)
    BlackEdges = []
    BlackEdges_copy = []
    for circle in Edges:
        for i in range(0,len(circle)-1,2):
            BlackEdges.append([circle[i],circle[i+1]])
            BlackEdges_copy.append([circle[i],circle[i+1]])
#    print(BlackEdges)
    GenomeGraph = ColoredEdges(P)
    with open('out.txt', 'w') as fh:
        print(GenomeGraph, file = fh)
    GenomeGraph = open('out.txt').read()
    GenomeGraph = GenomeGraph[1:-2]
    GenomeGraph = GenomeGraph.split('), (')
    GenomeGraph[0] = GenomeGraph[0].replace("(","")
    GenomeGraph[-1] = GenomeGraph[-1].replace(")","")
    genome_graph = []
    for group in GenomeGraph:
        group = group.split(', ')
        group = [int(x) for x in group]
        genome_graph.append(group)
    GenomeGraph = BreakOnGenomeGraph(genome_graph, indices)
#    print(GenomeGraph)
    edge_collection = GenomeGraph + BlackEdges
#    print(edge_collection)
    cycles = Cycles(edge_collection, BlackEdges)
    results = []
    # print(BlackEdges)
    # print(cycles)
    for cycle in cycles:
        t = []
        for blackedge in cycle:
            if blackedge in BlackEdges_copy or [blackedge[1], blackedge[0]] in BlackEdges_copy:
                t.append(blackedge[0])
                t.append(blackedge[1])
#        print(t)
#        print('|')
        tt = CycleToChromosome(t)
#        print(tt)
        results.append(tt)
    return results

text = open('dataset_8224_3.txt').read().split('\n')
genome = text[0]
genome = genome.split(')(')
indices = text[1]
indices = indices.split(', ')
indices = [int(x) for x in indices]
groups = []
for group in genome:
    group = group.replace("(","")
    group = group.replace(")","")
    group = group.split()
    group = [int(x) for x in group]
    groups.append(group)
results = BreakOnGenome(groups, indices)
for result in results:
    for i in range(len(result)):
        if result[i] > 0:
            result[i] = '+' + str(result[i])
    print('(', end = '')
    print(*result, end = '')
    print(')', end = '')
