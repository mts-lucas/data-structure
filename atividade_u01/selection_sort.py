# vetor = [5, 6, 4, 9, 11, 1]
# n = len(vetor)

import sys
import time


def selectionSort(vetor: list[int], n: int):

    for i in range(0, (n - 1)):
        m = i

        for j in range(i+1, n):

            if vetor[m] > vetor[j]:
                m = j

        vetor[i], vetor[m] = vetor[m], vetor[i]


if __name__ == "__main__":

    vetor = list(map(int, sys.argv[1:]))
    n = len(vetor) - 1
    start = time.time_ns()
    selectionSort(vetor, n)
    end = time.time_ns()
    final_time = end - start
