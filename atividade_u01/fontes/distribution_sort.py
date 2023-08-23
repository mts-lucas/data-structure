import sys
import time
# comment

from randomic_vetor import randVetor


def countingSort(v: list[int], n):
    b = max(v)
    c = [0] * (b + 1)
    w = [0] * n

    for i in range(n):
        c[v[i]] += 1

    for i in range(1, b + 1):
        c[i] += c[i - 1]

    for j in range(n - 1, -1, -1):
        w[c[v[j]] - 1] = v[j]
        c[v[j]] -= 1

    for i in range(n):
        v[i] = w[i]


if __name__ == "__main__":

    input = int(sys.argv[1])
    vetor = randVetor(input)
    n = len(vetor)
    start = time.time_ns()
    countingSort(vetor, n)
    end = time.time_ns()
    final_time = end - start
    print(final_time)
