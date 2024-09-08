import random


def BubbleSort(vetor, numero):
    if numero < 1:
        return

    for i in range(numero):
        if vetor[i] > vetor[i + 1]:
            temp = vetor[i]
            vetor[i] = vetor[i + 1]
            vetor[i + 1] = temp
    BubbleSort(vetor, numero - 1)


tamanho = 6
vetor = [0] * tamanho
for i in range(tamanho):
    num = 0
    while True:
        existe = False
        num = random.randrange(0, 61)
        p = 0

        while p < i:
            if vetor[p] == num:
                existe = True
                break
            p += 1
        if existe != True:
            break

    vetor[i] = num

BubbleSort(vetor, 5)
for i in range(tamanho):
    print(f"Numero ordenado: {vetor[i]}")
