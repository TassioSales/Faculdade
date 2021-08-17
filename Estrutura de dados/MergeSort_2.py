# Programa para implementar mergesort

import math  # para usar biblioteca math.inf


# função para tipo de fusão
# arr[l.. r] é a matriz que precisa ser classificada
# L e r são os índices esquerdo e direito de arr
def mergeSort(arr, l, r):
    if l < r:
        # encontrar índice médio de arr
        m = (l + r) // 2

        #   Classificar metade esquerda usando mergesort
        mergeSort(arr, l, m)

        #  Classificar metade direita usando tipo de mesclagem
        mergeSort(arr, m + 1, r)

        # mesclar o dois meio
        merge(arr, l, m, r)


# função para a fusão de duas sub matrizes de arr[l.. r]
def merge(arr, l, m, r):
    # comprimento da metade esquerda de arr
    nL = m - l + 1

    # comprimento da metade direita de arr
    nR = r - m

    # criar duas matrizes vazias L[0..nL] e R[0..nR]
    L = [0] * (nL + 1)
    R = [0] * (nR + 1)

    # cópia deixou metade de arr em L[0..nL-1]
    for i in range(0, nL):
        L[i] = arr[l + i]

    # copiar metade direita de arr em R[0..nR-1]
    for j in range(0, nR):
        R[j] = arr[m + 1 + j]

    # colocar infinito como valor sentinela no final de L e R
    L[nL] = math.inf
    R[nR] = math.inf

    # iterar sobre L e R
    # e copiar o menor de L[i] e R[j] para arr[k]
    i = 0
    j = 0
    for k in range(l, r + 1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1


# código do piloto para testar a implementação
A = [2, 3, 5, 1, 5, 9, 7, 2, 8]

mergeSort(A, 0, len(A) - 1)

print(A)  # saída: [1, 2, 2, 3, 5, 5, 7, 8, 9]