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

def MiddleEdge(v, w, top, bottom, left, right):
    w_l = []
    w_r = []
    for i in range(left,right):
        if i < (right+left)/2:
            w_l.append(w[i])
        else:
            w_r.append(w[i])
    w_l = "".join(w_l)
    w_r = "".join(w_r)
    S_l = MatrixBacktrack(match, mismatch, indel, v[top:bottom], w_l)[1]
    backtrack_r, S_r = MatrixBacktrack(match, mismatch, indel, v[top:bottom][::-1], w_r[::-1])
    Sum = {}
    for i in range(top,bottom+1):
        Sum[i] = S_l[(i,(right+left)/2)] + S_r[(len(v)-i,(right+left)/2)]
    max_value = max(Sum.values())
    for key in Sum.keys():
        if Sum[key] == max_value:
            middlenode = (key,int((right+left)/2))
    return middlenode, backtrack_r[bottom-top-middlenode[0],(right+left)/2]

def LinearSpaceAlignment(v, w, top, bottom, left, right):
    if left == right:
        print("↓")
        return "↓"
    elif top == bottom:
        print("→")
        return "→"
    else:
        middle = int((left+right)/2)                                        # take the integer
        midEdge = MiddleEdge(v, w, top, bottom, left, right)[1]
        midNode = MiddleEdge(v, w, top, bottom, left, right)[0][0]
        LinearSpaceAlignment(v, w, top, midNode, left, middle)
        print(midEdge)
        return midEdge
        if midEdge == "→" or midEdge == "↘":
            middle += 1
        if midEdge == "↓" or midEdge == "↘":
            midNode += 1
        LinearSpaceAlignment(v, w, midNode, bottom, middle, right)

text = open('test.txt').read().split('\n')
numbers = text[0].split()
match = int(numbers[0])
mismatch = int(numbers[1])
indel = int(numbers[2])
w = text[1]
v = text[2]
LinearSpaceAlignment(v, w, 0, len(v), 0, len(w))
print(LinearSpaceAlignment(v, w, 0, len(v), 0, len(w)))
