# l for lower, m for middle, u for upper
import math

def MatrixBacktrack_AffineGap(match, mismatch, opening_penalty, extension_penalty, v, w):
    S_m = {}
    S_l = {}
    S_u = {}
    backtrack = {}
    S_m[(0,0)] = 0
    S_l[(0,0)] = 0
    S_u[(0,0)] = 0
    S_l[(1,0)] = -opening_penalty
    S_m[(1,0)] = -opening_penalty
    S_u[(1,0)] = -math.inf
    backtrack[(1,0)] = "↓"
    S_u[(0,1)] = -opening_penalty
    S_m[(0,1)] = -opening_penalty
    S_l[(0,1)] = -math.inf
    backtrack[(0,1)] = "→"
    for i in range(2,len(v)+1):
        S_l[(i,0)] = S_l[(i-1,0)] - extension_penalty
        S_m[(i,0)] = S_m[(i-1,0)] - extension_penalty
        S_u[(i,0)] = -math.inf
        backtrack[(i,0)] = "↓"
    for j in range(2,len(w)+1):
        S_u[(0,j)] = S_u[(0,j-1)] - extension_penalty
        S_m[(0,j)] = S_m[(0,j-1)] - extension_penalty
        S_l[(0,j)] = -math.inf
        backtrack[(0,j)] = "→"
    for i in range(1,len(v)+1):
        for j in range(1,len(w)+1):
            t = 0
            if v[i-1] == w[j-1]:
                t = match
            else:
                t = -mismatch
            S_l[(i,j)] = max(S_l[(i-1,j)]-extension_penalty, S_m[(i-1,j)]-opening_penalty)
            S_u[(i,j)] = max(S_u[(i,j-1)]-extension_penalty, S_m[(i,j-1)]-opening_penalty)
            S_m[(i,j)] = max(S_l[(i,j)], S_u[(i,j)], S_m[(i-1,j-1)]+t)
            if S_m[(i,j)] == S_m[(i-1,j-1)]+t:
                backtrack[(i,j)] = "↘"
                S_u[(i,j)] = -math.inf
                S_l[(i,j)] = -math.inf
            elif S_m[(i,j)] == S_u[(i,j)]:
                backtrack[(i,j)] = "→"
                S_l[(i,j)] = -math.inf
            elif S_m[(i,j)] == S_l[(i,j)]:
                backtrack[(i,j)] = "↓"
                S_u[(i,j)] = -math.inf
    return backtrack, S_m

def Alignment(backtrack, v, w, i, j):
    str_v = []
    str_w = []
    while i != 0 or j != 0:
        if backtrack[(i,j)] == "↓":
            str_v.append(v[i-1])
            str_w.append("-")
            i -= 1
        elif backtrack[(i,j)] == "→":
            str_v.append("-")
            str_w.append(w[j-1])
            j -= 1
        else:
            str_v.append(v[i-1])
            str_w.append(w[j-1])
            i -= 1
            j -= 1
    return str_v, str_w

text = open("dataset_249_8.txt").read().split('\n')
#text = open("test.txt").read().split('\n')
numbers = text[0].split()
match = int(numbers[0])
mismatch = int(numbers[1])
opening_penalty = int(numbers[2])
extension_penalty = int(numbers[3])
v = text[1]
w = text[2]
result = MatrixBacktrack_AffineGap(match, mismatch, opening_penalty, extension_penalty, v, w)
backtrack = result[0]
score = result[1][len(v),len(w)]
print(score)
#print(backtrack)
str_v, str_w = Alignment(backtrack, v, w, len(v), len(w))
str_v.reverse()
str_w.reverse()
str_v = "".join(str_v)
str_w = "".join(str_w)
print(str_v)
print(str_w)
