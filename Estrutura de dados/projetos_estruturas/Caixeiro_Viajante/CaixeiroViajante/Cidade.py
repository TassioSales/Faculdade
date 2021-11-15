from random import random
import numpy as np


# classe Cidade --------------------------------------------------------------
class Cidade():
    def __init__(self, quantidade):
        self.quantidade = quantidade

    def gerarDistancias(self):
        qtd = self.quantidade
        cidade = np.zeros((qtd, qtd))
        # self.cidades = cidade
        for i in range(0, qtd):
            for j in range(0, qtd):
                if (i == j):
                    # Caso os indices forem iguais define 0 a distancia
                    # entre a cidade ex: cidade 1 esta a 0 de distancia da cidade 1
                    cidade[i][j] = 0
                else:
                    # Gera um valor aleatorio inteiro maior que 0 para
                    # distancia entra as cidades
                    valor = round(random() * 100) + 1
                    # Atribui o valor para o indice
                    cidade[i][j] = valor
                    x = j
                    y = i
                    # Atribui o mesmo valor para o indice invertido
                    cidade[x][y] = valor
            # Com isso garante que gere uma matriz simétrica para não
            # ficar com distancias diferentes entre as mesmas cidades
            i += 1
        self.cidades = cidade
        return self.cidades
