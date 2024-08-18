def ManhattanTourist(n, m, Down, Right):
    s = {}
    s[(0,0)] = 0
    for i in range(1,n+1):
        s[(i,0)] = s[(i-1,0)] + Down[i-1][0]
    for j in range(1,m+1):
        s[(0,j)] = s[(0,j-1)] + Right[0][j-1]
    for i in range(1,n+1):
        for j in range(1,m+1):
            s[(i,j)] = max((s[(i-1,j)]+Down[i-1][j]),(s[(i,j-1)]+Right[i][j-1]))
    return s[(n,m)]









text = open('dataset_261_10.txt').read().splitlines()
nm = text[0].split(' ')
n = int(nm[0])
m = int(nm[1])
Down = []
Right = []
for i in range(1,n+1):
    row = [int(x) for x in text[i].split()]
    Down.append(row)
for j in range(n+2,2*n+3):
    row = [int(x) for x in text[j].split()]
    Right.append(row)
print(ManhattanTourist(n, m, Down, Right))
