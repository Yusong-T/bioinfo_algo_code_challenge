import random
from collections import deque
import copy

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

def CycleToChromosome(nodes):
    chromosome = []
    for i in range(0,len(nodes),2):
        if nodes[i] < nodes[i+1]:
            chromosome.append(int(nodes[i+1]/2))
        else:
            chromosome.append(-(int(nodes[i]/2)))
    return chromosome

def ColoredEdges(groups):
    collections = []
    for group in groups:
        cycle = ChromosomeToCycle(group)
        cycle.append(cycle[0])
        for i in range(1,len(cycle),2):
            collections.append([cycle[i], cycle[i+1]])
    return collections

def BreakOnGenomeGraph(GenomeGraph, indices):
    # print(GenomeGraph)
    # print(indices)
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

def Cycles(edges, blackedges):
#    print(edges)
#    print(blackedges)
    edges_copy = edges.copy()
    blackedges_copy = blackedges.copy()
    cycles = []
    while len(blackedges_copy) != 0:
        cycle = []
        start_edge = random.choice(blackedges_copy)
        cycle.append(start_edge)
        edges_copy.remove(start_edge)
        blackedges_copy.remove(start_edge)
#        print(blackedges)
        edge_1 = start_edge
#        print(edge_1)
        flag = 0
        while flag != 1:
            for edge in edges_copy:
#                print(edge)
                if edge in blackedges_copy:
                    if edge[0] == edge_1[1]:
                        cycle.append(edge)
                        edge_1 = edge
                        edges_copy.remove(edge)
                        blackedges_copy.remove(edge)
                    elif edge[1] == edge_1[1]:
                        cycle.append([edge[1], edge[0]])
                        edge_1 = [edge[1], edge[0]]
                        edges_copy.remove(edge)
                        blackedges_copy.remove(edge)
                else:
                    if edge_1[1] == edge[0]:
                        cycle.append(edge)
                        edge_1 = edge
                        edges_copy.remove(edge)
                        if edge[1] == start_edge[0]:
                            flag = 1
                            break
                    elif edge_1[1] == edge[1]:
                        cycle.append([edge[1], edge[0]])
                        edge_1 = [edge[1], edge[0]]
                        edges_copy.remove(edge)
                        if edge[0] == start_edge[0]:
                            flag = 1
                            break
        cycles.append(cycle)
#        print(cycle)
    return cycles

def ShortestRearrangementScenario(P, Q):
    Edges = ChromosomeToCycle(P)
    BlackEdges = []
    for circle in Edges:
        for i in range(0,len(circle)-1,2):
            BlackEdges.append([circle[i],circle[i+1]])
    RedEdges = ColoredEdges(P)
    BlueEdges = ColoredEdges(Q)
    number = len(BlueEdges)
    Edges_collection = RedEdges + BlueEdges
    BreakPointGraph = Cycles(Edges_collection, BlueEdges)
    # iteration_collection = deque()
    # iteration_collection.append(BreakPointGraph)
    flag = 0
    while flag != 1:
        # index = 0
        # while index < len(iteration_collection):
        #     new_deque = deque()
        #     mark = 0
        #     BreakPointGraph = iteration_collection[index]
        #     if flag == 1 and mark == 1:
        #         break
        for cycle in BreakPointGraph:
            # while mark == 0:
            if len(BreakPointGraph) >= number:
                flag = 1
                # mark = 1
                break
            if len(cycle) > 2:
                for i in range(len(cycle)):
                    if cycle[i] in BlueEdges or [cycle[i][1], cycle[i][0]] in BlueEdges:
                        i_2 = cycle[i][0]
                        i_3 = cycle[i][1]
                        try:
                            i_1 = cycle[i-1][0]
                            try:
                                Edges_collection.remove(cycle[i-1])
                            except:
                                Edges_collection.remove([cycle[i-1][1], cycle[i-1][0]])
                        except:
                            i_1 = cycle[len(cycle)-1][0]
                            try:
                                Edges_collection.remove(cycle[len(cycle)-1])
                            except:
                                Edges_collection.remove([cycle[len(cycle)-1][1], cycle[len(cycle)-1][0]])
                        try:
                            i_4 = cycle[i+1][1]
                            try:
                                Edges_collection.remove(cycle[i+1])
                            except:
                                Edges_collection.remove([cycle[i+1][1], cycle[i+1][0]])
                        except:
                            i_4 = cycle[0][1]
                            try:
                                Edges_collection.remove(cycle[0])
                            except:
                                Edges_collection.remove([cycle[0][1], cycle[0][0]])
                        Edges_collection.append([i_1, i_4])
                        Edges_collection.append([i_2, i_3])
                        indices = [i_1,i_2,i_4,i_3]
                        BreakPointGraph = Cycles(Edges_collection, BlueEdges)
                        # BreakPointGraph_copy = BreakPointGraph.deepcopy()
                        BreakPointGraph_copy = copy.deepcopy(BreakPointGraph)
                        # new_deque.append(BreakPointGraph)
                        for circle in BreakPointGraph_copy:
                            for edge in circle:
                                if edge in BlueEdges or [edge[1], edge[0]] in BlueEdges:
                                    try:
                                        circle.remove(edge)
                                    except:
                                        circle.remove([edge[1], edge[0]])
                        RedEdges_collections = []
                        for circle in BreakPointGraph_copy:
                            for edge in circle:
                                RedEdges_collections.append(edge)
                        NewEdges = RedEdges_collections + BlackEdges
                        NewCycles = Cycles(NewEdges, BlackEdges)
                        genome = []
                        for circle in NewCycles:
                            genome_block = []
                            if len(circle) == 2:
                                for edge in circle:
                                    if edge in BlackEdges:
                                        genome_block.append(edge)
                            else:
                                for edge in circle:
                                    if edge in BlackEdges or [edge[1], edge[0]] in BlackEdges:
                                        genome_block.append(edge)
                            # genome_block.sort()
                            genome.append(genome_block)
                        results = []
                        for circle in genome:
                            result = []
                            for edge in circle:
                                if edge[0] < edge[1]:
                                    result.append(int((edge[1]/2)))
                                else:
                                    result.append(-int((edge[0]/2)))
                            results.append(result)
                        # print(results)
                        for result in results:
                            for i in range(len(result)):
                                if result[i] > 0:
                                    result[i] = '+' + str(result[i])
                            print('(', end = '')
                            print(*result, end = '')
                            print(')', end = '')
                        print('\n')
                        break
                    else:
                        continue
            else:
                continue
            # iteration_collection = new_deque.copy()
            # break


text = open('dataset_288_5.txt').read().split('\n')
P_raw = text[0]
print(P_raw)
Q_raw = text[1]
P_raw = P_raw.split(')(')
Q_raw = Q_raw.split(')(')
P_groups = []
for group in P_raw:
    group = group.replace("(","")
    group = group.replace(")","")
    group = group.split()
    group = [int(x) for x in group]
    P_groups.append(group)
Q_groups = []
for group in Q_raw:
    group = group.replace("(","")
    group = group.replace(")","")
    group = group.split()
    group = [int(x) for x in group]
    Q_groups.append(group)
ShortestRearrangementScenario(P_groups, Q_groups)
