vetor = [5, 6, 4, 2]
n = 4

for i in range(0, (n - 1)):
    m = i

    for j in range(i+1, n):

        if vetor[m] > vetor[j]:
            m = j

    vetor[i], vetor[m] = vetor[m], vetor[i]

print(vetor)
