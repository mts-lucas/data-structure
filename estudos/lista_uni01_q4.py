# Dado um vetor de inteiros, elabore um algoritmo que seja capaz de descobrir
# o indice do elemento medio
# do vetor, i.e. aquele que estaria na metade do vetor se ele estivesse
# ordenado. Por exemplo, para o vetor
# [0, 4, 7, 2, 3] o ındice do elemento medio seria o ultimo, pois 3 (tres)
# divide o vetor ao meio. Desenvolva
# um algoritmo que solucione o problema e calcule o tempo de execucao T(n)
#  do algoritmo.

vetor_de_inteiros = [0, 4, 7, 2, 3]


def midleElement(vetor: list[int]):
    maior: int = 1
    menor: int = 0
    medio: int = 0

    for i in range(len(vetor) - 1):
        if vetor[i] > maior:
            maior = vetor[i]
        elif vetor[i] < menor:
            menor = vetor[i]
        else:
            medio = i
    return medio


print(midleElement(vetor=vetor_de_inteiros))
