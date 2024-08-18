p = "CTACAGCAATACGATCATATGCGGATCCGCAGTGGCCGGTAGACACACGT"
q = "CTACCCCGCTGCTCAATGACCGGGACTAAAGAGGCGAAGATTATGGTGTG"

count = []
for i in range(0,len(p)):
    if p[i] == q[i]:
        continue
    else:
        count.append(i)

print(*(count))
print(len(count))
