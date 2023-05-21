vetor = [5, 6, 4, 2, 8, 1]

print(vetor)


def coutingSort(v: list[int], n):
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


coutingSort(vetor, len(vetor))
print(vetor)
