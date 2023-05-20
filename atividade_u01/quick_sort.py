vetor = [5, 6, 4, 2, 8, 1]

print(vetor)


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


quickSort(vetor, 0, (len(vetor) - 1))
print(vetor)
