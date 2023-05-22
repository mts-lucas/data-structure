from random import randint


def randVetor(n):

    vetor = []
    for i in range(0, n):
        vetor.append(randint(1, 10000))

    return vetor
