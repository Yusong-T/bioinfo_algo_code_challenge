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

def overlap(f_edge, l_edge):
    if f_edge[0]==l_edge[0] or f_edge[0]==l_edge[1] or f_edge[1]==l_edge[0] or f_edge[1]==l_edge[1]:
        return 1
    else:
        return 0

def non_trivial_cycle(edge):
    reverse_edge = (edge[1], edge[0])
    return (edge, reverse_edge)

def Cycles(edges):
    count = 0
    seen = []
    pairs = []
    for edge in edges:
        edge_p = non_trivial_cycle(edge)
        if edge_p[0] in seen or edge_p[1] in seen:
            pairs.append(edge)
            try:
                seen.remove(edge_p[0])
            except:
                seen.remove(edge_p[1])
        else:
            seen.append(edge)
    count += len(pairs)
#    print(pairs)
#    print(seen)
    while len(seen) != 0:
        cycle = []
        start_edge = random.choice(seen)
        cycle.append(start_edge)
        seen.remove(start_edge)
        edge_1 = start_edge
        flag = 0
        while flag != 1:
            for edge in seen:
                if overlap(edge_1, edge) == 1 and overlap(start_edge, edge) == 1 and len(cycle) > 1:
                    cycle.append(edge)
                    seen.remove(edge)
                    flag = 1
                    break
                if overlap(edge_1, edge) == 1:
                    cycle.append(edge)
                    edge_1 = edge
                    seen.remove(edge)
        # print(cycle)
        # print("///")
        # print(seen)
        count += 1
    return count

def BreakDistance(P_groups, Q_groups):
    P_colored_edges = ColoredEdges(P_groups)
    Q_colored_edges = ColoredEdges(Q_groups)
    edge_collections = P_colored_edges + Q_colored_edges
#    print(edge_collections)
    blocks = len(P_colored_edges)
    cycles_count = Cycles(edge_collections)
#    print(cycles_count)
    distance = blocks - cycles_count
    return distance


text = open('dataset_288_4.txt').read().split('\n')
P_text = text[0]
Q_text = text[1]
P_text = P_text.split(')(')
Q_text = Q_text.split(')(')
P_groups = []
Q_groups = []
for group in P_text:
    group = group.replace("(","")
    group = group.replace(")","")
    group = group.split()
    group = [int(x) for x in group]
    P_groups.append(group)
for group in Q_text:
    group = group.replace("(","")
    group = group.replace(")","")
    group = group.split()
    group = [int(x) for x in group]
    Q_groups.append(group)
print(BreakDistance(P_groups, Q_groups))
