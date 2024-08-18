
def Reversal(str):
    str.reverse()
    str = [-x for x in str]
    return str

def GreedySorting(P):
    permutations = []
    for k in range(len(P)):
        if abs(P[k]) != k+1:
            for t in range(len(P)):
                if abs(P[t]) == k+1:
                    index = t
            P = P[:k] + Reversal(P[k:index+1]) + P[index+1:]
            permutations.append(P)
        if P[k] == -(k+1):
            P = P[:k] + [k+1] + P[k+1:]
            permutations.append(P)
    return permutations



text = open('dataset_286_4.txt').read().split()
sequence = [int(x) for x in text]
output = GreedySorting(sequence)
for string in output:
    for i in range(len(string)):
        if string[i] > 0:
            string[i] = str('+')+str(string[i])
    print(*string)
