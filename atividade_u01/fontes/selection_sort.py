import sys
import time

from randomic_vetor import randVetor


def selectionSort(vetor: list[int], n: int):

    for i in range(0, (n - 1)):
        m = i

        for j in range(i+1, n):

            if vetor[m] > vetor[j]:
                m = j

        vetor[i], vetor[m] = vetor[m], vetor[i]


if __name__ == "__main__":

    input = int(sys.argv[1])
    vetor = randVetor(input)
    n = len(vetor)
    start = time.time_ns()
    selectionSort(vetor, n)
    end = time.time_ns()
    final_time = end - start
    print(final_time)
