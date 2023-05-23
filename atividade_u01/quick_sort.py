# vetor = [5, 6, 4, 2, 8, 1]

import sys
import time

# caso medio
# from randomic_vetor import randVetor

# pior caso 
from randomic_vetor import invertVetor


def partition(v: list[int], s: int, e: int) -> int:
    d = s - 1

    for j in range(s, e):
        if v[j] <= v[e]:
            d += 1
            v[j], v[d] = v[d], v[j]

    v[e], v[(d + 1)] = v[(d + 1)], v[e]
    return (d + 1)


def quickSort(v: list[int], s: int, e: int):
    if (s < e):
        p = partition(v, s, e)
        quickSort(v, s, (p - 1))
        quickSort(v, (p + 1), e)


if __name__ == "__main__":

    input = int(sys.argv[1])
    # caso medio
    # vetor = randVetor(input)

    # pior caso
    vetor = invertVetor(input)

    e = len(vetor) - 1
    start = time.time_ns()
    quickSort(vetor, 0, e)
    end = time.time_ns()
    final_time = end - start
    print(final_time)
