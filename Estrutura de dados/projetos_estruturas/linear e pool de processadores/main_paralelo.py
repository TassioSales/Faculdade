from Linear.Paralelos import fibonacci_sequence_of_paralelos
from multiprocessing import Pool
import time

input_number = input("Coloque vírgulas se desejar mais de um valor \nFabonacci: ")
input_values = []
input_values = input_number.split(",")
toc = time.time()

pool = Pool()

result = pool.map(fibonacci_sequence_of_paralelos, input_values)
tic = time.time()

time_taken = round((tic - toc) * 1000, 1)
print("Demorou {} milissegundos para calcular os fibonaccis de {} com paralelismo de processador ".format(time_taken,
                                                                                                          input_number))

pool.close()
pool.join()