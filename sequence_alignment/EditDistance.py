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

def hammingdis(p,q):
    count = []
    for i in range(0,len(p)):
        if p[i] == q[i]:
            continue
        else:
            count.append(i)
    return len(count)


text = open('dataset_248_3.txt').read().split('\n')
v = text[0]
w = text[1]
match = 0
mismatch = 1
indel = 1
result = MatrixBacktrack(match, mismatch, indel, v, w)
backtrack = result[0]
str_v, str_w = Alignment(backtrack, v, w, len(v), len(w))
str_v.reverse()
str_w.reverse()
str_v = "".join(str_v)
str_w = "".join(str_w)
print(hammingdis(str_v, str_w))
