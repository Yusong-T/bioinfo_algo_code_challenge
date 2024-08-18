fname = input("Enter file name:")
fh = open(fname)
otext = []
text = "".join(otext)               # turns list into a string
for line in fh:
    text = text + line
k = int(input("k:\n"))
L = int(input("L:\n"))
t = int(input("t:\n"))

def ftable(text,k):                 # gives the counts of each pattern
    fmap = {}
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        if pattern in fmap:
            fmap[pattern] += 1
        else:
            fmap[pattern] = 1
    return fmap

# def f_words(text,k):
#     fpatterns = []
#     fmap = ftable(text,k)
#     Max = max(fmap.values())
#     for key,value in fmap.items():
#         if value == Max:
#             fpatterns.append(key)
#     return fpatterns

patterns = []
count = 0
for i in range(len(text)-L+1):
	window = text[i:i+L]
	freqmap = ftable(window,k)
	for key in freqmap:
		if freqmap[key] >= t and key not in patterns:
			patterns.append(key)
			count = count + 1

print(count)
print(len(patterns))
print(*list(set(patterns)))
