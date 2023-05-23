from random import randint


def randVetor(n):

    vetor = []
    for i in range(0, n):
        vetor.append(randint(1, 10000))

    return vetor


#  pior caso insertion e quick
def invertVetor(n):

    vetor = []
    for i in range(n, -1, -1):
        vetor.append(i)
    return vetor


# melhor caso insertion
def sortVetor(n):
    vetor = []
    for i in range(n):
        vetor.append(i)
    return vetor
