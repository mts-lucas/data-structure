# vetor = [5, 6, 4, 2, 8, 1]

# print(vetor)
# print(len(vetor))
import sys
import time


def merge(v: list[int], s: int, m: int, e: int) -> list[int]:
    p = s
    q = m + 1
    w: list[int] = []
    for i in range(0, (e - s + 1)):
        if (q > e) or ((p <= m) and (v[p] < v[q])):
            w.append(v[p])
            p += 1
        else:
            w.append(v[q])
            q += 1

    for i in range(0, (e - s + 1)):
        v[(s + i)] = w[i]
    return v


def mergeSort(v: list[int], s: int, e: int) -> list[int]:
    if (s < e):
        m: int = (s + e)//2
        mergeSort(v, s, m)
        mergeSort(v, (m + 1), e)
        merge(v, s, m, e)
    return v


if __name__ == "__main__":

    vetor = list(map(int, sys.argv[1:]))
    e = len(vetor) - 1
    start = time.time_ns()
    mergeSort(vetor, 0, e)
    end = time.time_ns()
    final_time = end - start
    print(final_time)
