import math

AminoAcidMass = {
    'G': 57,
    'A': 71,
    'S': 87,
    'P': 97,
    'V': 99,
    'T': 101,
    'C': 103,
    'I': 113,
    'N': 114,
    'D': 115,
    'K': 128,
    'E': 129,
    'M': 131,
    'H': 137,
    'F': 147,
    'R': 156,
    'Y': 163,
    'W': 186
}
Mass = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]

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

def CycloSpectrum(Peptide, AminoAcidMass):
    PrefixMass = {}
    PrefixMass[0] = 0
    for i in range(1,len(Peptide)+1):
        for aa in AminoAcidMass.keys():
            if Peptide[i-1] == aa:
                PrefixMass[i] = PrefixMass[i-1] + AminoAcidMass[aa]
    peptideMass = PrefixMass[len(Peptide)]
    CyclicSpectrum = [0]
    for i in range(len(Peptide)):
        for j in range(i+1,len(Peptide)+1):
            CyclicSpectrum.append(PrefixMass[j]-PrefixMass[i])
            if i>0 and j<len(Peptide):
                CyclicSpectrum.append(peptideMass-(PrefixMass[j]-PrefixMass[i]))
    CyclicSpectrum.sort()
    return CyclicSpectrum

def Score(Theoretical,Experimental):
    score = 0
    for i in Experimental:
        if i in Theoretical:
            score += 1
            Theoretical.remove(i)
    return score

def Mass(Peptide,AminoAcidMass):
    mass = 0
    for i in Peptide:
        mass += AminoAcidMass[i]
    return mass

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

def LeaderboardCyclopeptideSequencing(Spectrum, N):                                     # can NOT remove items from a list while iterating itself
    ParentMass = max(Spectrum)
    Leaderboard = ['']
    LeaderPeptide = ''
    result_Peptide = []
    while len(Leaderboard) != 0:
        for i in Leaderboard[:]:                                                        # !!!loops over a copy
            for aa in AminoAcidMass.keys():
                Leaderboard.append(i+aa)
            Leaderboard.remove(i)
        Leaderboard = Trim(Leaderboard,Spectrum,N)
        for Peptide in Leaderboard[:]:                                                  # !!!loops over a copy
            if Mass(Peptide,AminoAcidMass) == ParentMass:
                if Score(CycloSpectrum(Peptide,AminoAcidMass),Spectrum) >= Score(CycloSpectrum(LeaderPeptide,AminoAcidMass),Spectrum):
                    LeaderPeptide = Peptide
                    result_Peptide.append(Peptide)
            elif Mass(Peptide,AminoAcidMass) > ParentMass:
                Leaderboard.remove(Peptide)
#        Leaderboard = Trim(Leaderboard,Spectrum,N)
#        N = math.ceil(N*0.89275)                                                             # modifies N to save a lot of time
    output = []
    for peptide in result_Peptide:
        result = []
        for i in peptide:
            result.append(AminoAcidMass[i])
        result = [str(x) for x in result]
        result = "-".join(result)
        output.append(result)
    output = [*set(output)]
    print(len(output))
    return output





text = open('test.txt').read().split('\n')
N = int(text[0])
Spectrum = text[1].split()
Spectrum = [int(x) for x in Spectrum]
print(*LeaderboardCyclopeptideSequencing(Spectrum, N))
