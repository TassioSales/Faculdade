from random import random
from random import randint
import matplotlib.pyplot as plt
import numpy as np

# classe Populacao --------------------------------------------------------------
class Individuos():
    def __init__(self, tamanhoPopulacao, quantidade):
        self.tamanhoPopulacao = tamanhoPopulacao
        self.quantidade = quantidade

    def geraCromossomo(self):
        cromossomo = []
        populacao = []
        quantidade = self.quantidade
        tamanhoPopulacao = self.tamanhoPopulacao
        x = 1
        for x in range(tamanhoPopulacao):
            # Cria o cromossomo com numeros aleatórios, cromossomo sempre
            # do mesmo tamanho que o nº de cidades
            while len(cromossomo) != quantidade:
                # Faz o sorteio dos números aleatoriamente
                r = randint(1, quantidade)
                if r not in cromossomo:
                    # Garante que não vai haver repetição
                    cromossomo.append(r)
            # Jogaga o cidadão gerado para a lista da população
            populacao.append(cromossomo)
            cromossomo = []
        self.populacao = populacao
        return self.populacao

    def geraFitness(self, populacao, cidades):
        fitness = []
        quantidade = self.quantidade
        tamanhoPopulacao = self.tamanhoPopulacao
        for i in range(tamanhoPopulacao):
            # Variaveis temporarias
            temp = []
            nota = 0
            x = 0
            y = 0
            temp = populacao[i]
            # Se estiver no alcance vai fazendo a conta das distancias e somando
            for j in range(quantidade - 1):
                x = temp[j]
                if (j < quantidade):
                    y = temp[j + 1]
                else:
                    y = -1
                if (y > 0):
                    nota += cidades[x - 1][y - 1]
            # Grava o Fitness
            fitness.append(nota)
        self.fitness = fitness
        return self.fitness

    def ordenaPopulacao(self, populacao, cidades):
        # ordenar populacao por fitness
        # Passa o cromossso da população e o fitness para uma Lista temporária
        temp = []
        if (len(populacao) == 0):
            populacao = self.geraCromossomo()
        fitness = self.geraFitness(populacao, cidades)
        temp = list(zip(fitness, populacao))
        # Passa para a lista temporaria para uma nova lista já ordenando de acordo com o Fitness
        lista_tupla_ordenada = []
        lista_tupla_ordenada = sorted(temp, reverse=False)
        self.litsta_ordanada = lista_tupla_ordenada
        return self.litsta_ordanada

    def reproducao(self, populacao, cidades):
        novaPopulacao = []
        if (len(populacao) == 0):
            populacao = self.geraCromossomo()
        quantidade = self.quantidade
        tamanhoPopulacao = self.tamanhoPopulacao
        lista_tupla_ordenada = self.ordenaPopulacao(populacao, cidades)
        for i in range(0, tamanhoPopulacao, 2):
            # Distribui a população com melhor fitness para gerar novos filhos
            pai1 = []
            pai2 = []
            cromfilho = []
            filho1 = []
            filho2 = []
            pai1 = lista_tupla_ordenada[i][1]
            # Condição para reprodução
            if (i < tamanhoPopulacao - 1):
                pai2 = lista_tupla_ordenada[i + 1][1]
            else:
                pai2 = lista_tupla_ordenada[-1][1]
            for x in range(quantidade):
                # Sorteio para definir se vai erdar do pai1 ou do pai2
                if random() < 0.7:
                    cromfilho.append("0")
                else:
                    cromfilho.append("1")

            # FILHO1
            for j in range(quantidade):
                # Erda do pai1
                if cromfilho[j] == "1":
                    filho1.append(pai1[j])
                # Erda do pai2
                else:
                    filho1.append(0)
            for j in range(quantidade):
                z = 0
                # No caso de erdar do pai2 os cromossomos
                if filho1[j] == 0:
                    while (z != quantidade):
                        # Garantia de não repetição de cromossomo
                        if pai2[z] not in filho1:
                            # Vai ficar rodando até achar um cromssomo do pai2 que ainda não está no filho1
                            filho1[j] = pai2[z]
                            z = quantidade
                        else:
                            z = z + 1
            filho1 = self.mutacao(filho1)

            # FILHO2
            for j in range(quantidade):
                if cromfilho[j] == "1":
                    # Erda do pai1
                    filho2.append(pai2[j])
                else:
                    # Erda do pai2
                    filho2.append(0)
            for j in range(quantidade):
                z = 0
                # No caso de erdar do pai2 os cromossomos
                if filho2[j] == 0:
                    while (z != quantidade):
                        # Garantia de não repetição de cromossomo
                        if pai1[z] not in filho2:
                            # Vai ficar rodando até achar um cromssomo do pai2 que ainda não está no filho2
                            filho2[j] = pai1[z]
                            z = quantidade
                        else:
                            z = z + 1
            filho2 = self.mutacao(filho2)

            novaPopulacao.append(filho1)
            novaPopulacao.append(filho2)

        litsta_ordanada = self.ordenaPopulacao(novaPopulacao, cidades)
        self.litsta_ordanada = litsta_ordanada
        return self.litsta_ordanada

    def mutacao(self, filho):
        taxaMult = random()
        quantidade = self.quantidade
        if taxaMult < 0.01:
            # Cria um random para fazer multação
            indice1 = randint(0, (quantidade - 1))
            indice2 = randint(0, (quantidade - 1))
            temp = filho[indice1]
            temp2 = filho[indice2]
            filho[indice1] = temp2
            filho[indice2] = temp
        return filho
