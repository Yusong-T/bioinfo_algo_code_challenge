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




text = open('dataset_8222_4.txt').read().strip("(").strip(")").split()
text[len(text)-1] = text[len(text)-1].replace(")","")                   # remove the ')' at the end
text = [int(x) for x in text]
print('(', end = '')
print(*ChromosomeToCycle(text), end = '')
print(')')
