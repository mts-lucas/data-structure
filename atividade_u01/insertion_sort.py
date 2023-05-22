# vetor = [5, 6, 4, 2]
# n = 4
import sys
import time

from randomic_vetor import randVetor

# pior caso
# from randomic_vetor import invertVetor

# melhor caso
# from randomic_vetor import sortVetor


def insertionSort(vetor: list[int], n: int):
    for e in range(1, n):
        i: int = e
        while (i > 0) and vetor[i-1] > vetor[i]:
            vetor[i], vetor[i-1] = vetor[i-1], vetor[i]
            i -= 1


if __name__ == "__main__":

    input = int(sys.argv[1])

    # caso medio
    vetor = randVetor(input)

    # pior caso
    # vetor = invertVetor(input)

    # melhor caso
    # vetor = sortVetor(input)

    n = len(vetor)
    start = time.time_ns()
    insertionSort(vetor, n)
    end = time.time_ns()
    final_time = end - start
    print(final_time)
