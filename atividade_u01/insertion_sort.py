vetor = [5, 6, 4, 2]
n = 4

for e in range(1, n):
    i = e
    while (i > 0) and vetor[i-1] > vetor[i]:
        vetor[i], vetor[i-1] = vetor[i-1], vetor[i]
        i -= 1

print(vetor)
