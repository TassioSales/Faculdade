import matplotlib.pyplot as plt
import time
from CaixeiroViajante.AlgoritimoGenetico import AlgoritimoGenetico

quantidade = int(input("Digite a quantidade de cidades (+ que duas): "))
while quantidade < 2:
    print("Quantidade invalida!!!")
    quantidade = int(input("Digite a quantidade de cidades (+ que duas): "))

tamanhoPopulacao = int(input("Digite o tamanho da população (+ que um):  "))
while tamanhoPopulacao < 1:
    print("Quantidade invalida!!!")
    tamanhoPopulacao = int(input("Digite o tamanho da população (+ que um): "))

geracoes = int(input("Digite a quantidade de gerações (+ que uma): "))
while geracoes < 1:
    print("Quantidade invalida!!!")
    geracoes = int(input("Digite a quantidade de gerações (+ que uma): "))

inicio = time.time()
ag = AlgoritimoGenetico(tamanhoPopulacao, quantidade, geracoes)
teste = ag.resolver()
print("Resultado: ", teste[0])
plt.plot(ag.melhores)
plt.title("Acompanhamento dos valores.\n Valor em Km, quanto menor melhor")
plt.show()
fim = time.time()
total_time = fim - inicio
print(f"O tempo de excução do Caixeiro Viajante foi foi {total_time:.2f}")