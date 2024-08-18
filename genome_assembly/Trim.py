AminoAcidMass = {
    'G': 57,
    'A': 71,
    'S': 87,
    'P': 97,
    'V': 99,
    'T': 101,
    'C': 103,
    'I': 113,
    'L': 113,
    'N': 114,
    'D': 115,
    'K': 128,
    'Q': 128,
    'E': 129,
    'M': 131,
    'H': 137,
    'F': 147,
    'R': 156,
    'Y': 163,
    'W': 186
}

def LinearSpectrum(Peptide, AminoAcidMass):
    PrefixMass = {}
    PrefixMass[0] = 0
    for i in range(1,len(Peptide)+1):
        for aa in AminoAcidMass.keys():
            if Peptide[i-1] == aa:
                PrefixMass[i] = PrefixMass[i-1] + AminoAcidMass[aa]
    LinearSpectrum = [0]
    for i in range(len(Peptide)):
        for j in range(i+1,len(Peptide)+1):
            LinearSpectrum.append(PrefixMass[j]-PrefixMass[i])
    LinearSpectrum.sort()
    return LinearSpectrum


def Score(Theoretical,Experimental):
    score = 0
    for i in Experimental:
        if i in Theoretical:
            score += 1
            Theoretical.remove(i)
    return score

def Trim(Leaderboard,Spectrum,N):
    LinearScores = {}
    for j in range(len(Leaderboard)):
        Peptide = Leaderboard[j]
        LinearScores[Peptide] = Score(LinearSpectrum(Peptide,AminoAcidMass),Spectrum)
    LinearScores = sorted(LinearScores.items(), key=lambda item: item[1], reverse=True)
    for j in range(N,len(Leaderboard)):
        if LinearScores[j][1] < LinearScores[N-1][1]:
            Leaderboard.remove(LinearScores[j][0])
    return Leaderboard


text = open('dataset_4913_3.txt').read().split('\n')
Leaderboard = text[0].split()
Spectrum = text[1].split()
Spectrum = [int(x) for x in Spectrum]
N = int(text[2])

print(*Trim(Leaderboard,Spectrum,N))
