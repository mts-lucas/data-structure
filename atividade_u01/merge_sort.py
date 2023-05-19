vetor = [5, 6, 4, 2, 8, 1]
n = 4


def merge(v: list[int], s: int, m: int, e: int):
    p = s
    q = m + 1
    w: list[int] = []
    for j in range(0, (e - s + 1)):
        if (q > e) or ((p <= m) and (v[p] < v[q])):
            w.append(v[p])
            p += 1
        else:
            w.append(v[q])
            q += 1

    for k in range(0, (e - s + 1)):
        v[(s + k - 1)] = w[k]
    return v


def mergeSort(v: list[int], s: int, e: int):
    if (s < e):
        m: int = (s + e)//2
        mergeSort(v, s, m - 1)
        mergeSort(v, (m + 1), e)
        merge(v, s, m, e)
    return v
