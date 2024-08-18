def Breakpoints(P):
    P = [0] + P + [int(len(P)+1)]
    count = 0
    for i in range(len(P)-1):
        if P[i] + 1 != P[i+1]:
            count += 1
    return count





text = open('dataset_287_6.txt').read().split()
sequence = [int(x) for x in text]
print(Breakpoints(sequence))
