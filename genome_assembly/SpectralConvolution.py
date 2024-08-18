def SpectralConvolution(Spectrum):
    convolution = []
    for i in range(1,len(Spectrum)):
        for j in range(0,i):
            if (Spectrum[i]-Spectrum[j]) != 0:
                convolution.append(Spectrum[i]-Spectrum[j])
    return convolution




Spectrum = open('dataset_104_4.txt').read().split()
Spectrum = [int(x) for x in Spectrum]
print(*SpectralConvolution(Spectrum))
