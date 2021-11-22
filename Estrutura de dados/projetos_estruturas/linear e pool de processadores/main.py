from Linear.linear import fibonacci_sequence_of_linear
from Linear.Paralelos import fibonacci_sequence_of_paralelos
from multiprocessing import Pool
import time


def linear():
    input_number = input("Coloque vírgulas se desejar mais de um valor \nFabonacci: ")
    input_values = []
    input_values = input_number.split(",")
    toc = time.time()
    for i in input_values:
        fibonacci_sequence_of_linear(i)
    tic = time.time()
    time_taken = round((tic - toc) * 1000, 1)
    print(
        f"{time_taken} milissegundos para calcular fibonacci da lista {input_number} na versão monoprocessada linear.")


def paralelos():
    input_number = input("Coloque vírgulas se desejar mais de um valor \nFabonacci: ")
    input_values = []
    input_values = input_number.split(",")
    toc = time.time()

    pool = Pool()

    result = pool.map(fibonacci_sequence_of_paralelos, input_values)
    tic = time.time()

    time_taken = round((tic - toc) * 1000, 1)
    print(F"Demorou {time_taken} milissegundos para calcular os fibonaccis de {input_number} com paralelismo de processador ")

    pool.close()
    pool.join()


def main():
    print("#" * 13)
    print("## FUNÇÕES ##")
    print("#" * 13)
    print("1 - Para execultar linear")
    print("2 - Para execultar Paralelo")
    opcao = int(input("Qual função deseja execultar: "))
    while True:
        try:
            if opcao == 1:
                linear()
            if opcao == 2:
                paralelos()
        except Exception as erro:
            print("Opção invalida")
            print(erro)
            print(erro.__class__)
main()
