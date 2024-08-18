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

text = open('dataset_8222_7.txt').read().split(')(')
groups = []
for group in text:
    group = group.replace("(","")
    group = group.replace(")","")
    group = group.split()
    group = [int(x) for x in group]
    groups.append(group)
result = ColoredEdges(groups)
print(result)
