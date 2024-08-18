import sys
sys.setrecursionlimit(1500)                         # to increase recursion depth

def LCSBackTrack(v, w):
    S = {}
    backtrack = {}
    for i in range(len(v)+1):
        S[(i,0)] = 0
    for j in range(len(w)+1):
        S[(0,j)] = 0
    for i in range(1,len(v)+1):
        for j in range(1,len(w)+1):
            match = 0
            if v[i-1] == w[j-1]:
                match = 1
            S[(i,j)] = max(S[i-1,j],S[i,j-1],(S[(i-1,j-1)]+match))
            if S[(i,j)] == S[(i-1,j)]:
                backtrack[i,j] = "↓"
            elif S[(i,j)] == S[(i,j-1)]:
                backtrack[i,j] = "→"
            elif S[(i,j)] == S[(i-1,j-1)] + match:
                backtrack[i,j] = "↘"
    return backtrack

def OutputLCS(backtrack, v, i, j):
    if i == 0 or j == 0:
        return ""
    if backtrack[(i,j)] == "↓":
        return OutputLCS(backtrack, v, i-1, j)
    elif backtrack[(i,j)] == "→":
        return OutputLCS(backtrack, v, i, j-1)
    else:
        return OutputLCS(backtrack, v, i-1, j-1) + v[i-1]



text = open('dataset_245_5.txt').read().split('\n')
s = text[0]
t = text[1]
backtrack = LCSBackTrack(s, t)
print(OutputLCS(backtrack, s, len(s), len(t)))
