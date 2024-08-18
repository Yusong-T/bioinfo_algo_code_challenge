pattern = 'CGC'
genome = 'ATGACTTCGCTGTTACGCGC'


k = len(pattern)
positions = []
for i in range(len(genome)-k+1):
	if genome[i:i+k] == pattern:
		positions.append(i)
print(*positions)

