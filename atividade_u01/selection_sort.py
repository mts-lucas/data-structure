vetor = [5, 6, 4, 9, 11, 1]
n = len(vetor)


def selectionSort(vetor: list[int], n: int):

    for i in range(0, (n - 1)):
        m = i

        for j in range(i+1, n):

            if vetor[m] > vetor[j]:
                m = j

        vetor[i], vetor[m] = vetor[m], vetor[i]


selectionSort(vetor, n)
print(vetor)
