# # finding matched pattern
# def patternmatch(text, pattern):
#     positions = []
#     count = 0
#     space = len(pattern)
#     end = len(text) + 1                      # think about why '+1'
#     for i in range(end-space):
#         if text[i:i+space] == pattern:
#             count += 1
#             positions.append(i+1)            # again think about why '+1'

#     return count, positions

# dna = input('The DNA sequence:\n')
# ori = input('The pattern:\n')


# count, positions = patternmatch(dna, ori)
# print(count, positions)


# finding frequent words /my_version
text = input("The DNA sequence:\n")
k = input("k:\n")
k = int(k)

def ftable(text,k):
    fmap = {}
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        if pattern in fmap:
            fmap[pattern] += 1
        else:
            fmap[pattern] = 1
    return fmap

def f_words(text,k):
    fpatterns = []
    fmap = ftable(text,k)
    Max = max(fmap.values())
    for key,value in fmap.items():
        if value == Max:
            fpatterns.append(key)
    return fpatterns


print(f_words(text,k))
