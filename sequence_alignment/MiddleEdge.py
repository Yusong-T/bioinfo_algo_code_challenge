def MatrixBacktrack(match, mismatch, indel, v, w):
    S = {}
    backtrack = {}
    S[(0,0)] = 0
    for i in range(1,len(v)+1):
        S[(i,0)] = S[(i-1,0)] - indel
        backtrack[(i,0)] = "↓"
    for j in range(1,len(w)+1):
        S[(0,j)] = S[(0,j-1)] - indel
        backtrack[(0,j)] = "→"
    for i in range(1,len(v)+1):
        for j in range(1,len(w)+1):
            t = 0
            if v[i-1] == w[j-1]:
                t = match
            else:
                t = -mismatch
            S[(i,j)] = max(S[(i-1,j)]-indel, S[(i,j-1)]-indel, S[(i-1,j-1)]+t)
            if S[(i,j)] == S[(i-1,j)]-indel:
                backtrack[i,j] = "↓"
            elif S[(i,j)] == S[(i,j-1)]-indel:
                backtrack[i,j] = "→"
            elif S[(i,j)] == S[(i-1,j-1)]+t:
                backtrack[i,j] = "↘"
    return backtrack, S



text = open('dataset_250_12.txt').read().split('\n')
numbers = text[0].split()
match = int(numbers[0])
mismatch = int(numbers[1])
indel = int(numbers[2])
w = text[1]
v = text[2]
w_l = []
w_r = []
for i in range(0,len(w)):
    if i < len(w)/2:
        w_l.append(w[i])
    else:
        w_r.append(w[i])
w_l = "".join(w_l)
w_r = "".join(w_r)
S_l = MatrixBacktrack(match, mismatch, indel, v, w_l)[1]
backtrack_r, S_r = MatrixBacktrack(match, mismatch, indel, v[::-1], w_r[::-1])
Sum = {}
for i in range(len(v)+1):
    Sum[i] = S_l[(i,len(w)/2)] + S_r[(len(v)-i,len(w)/2)]
max_value = max(Sum.values())
for key in Sum.keys():
    if Sum[key] == max_value:
        middlenode = (key,int(len(w)/2))
if backtrack_r[len(v)-middlenode[0],len(w)/2] == '→':
    middlenode_2 = (middlenode[0],middlenode[1]+1)
elif backtrack_r[len(v)-middlenode[0],len(w)/2] == '↘':
    middlenode_2 = (middlenode[0]+1,middlenode[1]+1)
print(*middlenode)
print(*middlenode_2)
