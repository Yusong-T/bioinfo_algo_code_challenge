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

# def Alignment(backtrack, v, w, i, j):
#     if i == 0 and j == 0:
#         return "", ""
#     if backtrack[(i,j)] == "↓":
#         return Alignment(backtrack, v, w, i-1, j)+v[i-1], Alignment(backtrack, v, w, i-1, j)+"-"
#     elif backtrack[(i,j)] == "→":
#         return Alignment(backtrack, v, w, i, j-1)+"-", Alignment(backtrack, v, w, i, j-1)+w[j-1]
#     else:
#         return Alignment(backtrack, v, w, i-1, j-1)+v[i-1], Alignment(backtrack, v, w, i-1, j-1)+w[i-1]

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



text = open("dataset_247_3.txt").read().split('\n')
numbers = text[0].split()
match = int(numbers[0])
mismatch = int(numbers[1])
indel = int(numbers[2])
v = text[1]
w = text[2]
result = MatrixBacktrack(match, mismatch, indel, v, w)
backtrack = result[0]
score = result[1][len(v),len(w)]
print(score)
str_v, str_w = Alignment(backtrack, v, w, len(v), len(w))
str_v.reverse()
str_w.reverse()
str_v = "".join(str_v)
str_w = "".join(str_w)
print(str_v)
print(str_w)
