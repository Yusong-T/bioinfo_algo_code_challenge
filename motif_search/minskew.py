fname = input("Enter file name:")
fh = open(fname)
otext = []
text = "".join(otext)
for line in fh:
    text = text + line              # obtains the whole string of genome

skew = 0
i = 1
count = {}
for g in text:
    while True:
        if g == "C":
            skew -= 1
        elif g == "G":
            skew += 1
        break
    count[i] = skew
    i = i + 1


m = min(count.values())
pos = []
for key in count.keys():
    if count[key] == m:
        pos.append(key)


print(*(pos))
