from Linear.linear import fibonacci_sequence_of_linear
import time

input_number = input("Coloque vírgulas se desejar mais de um valor \nFabonacci: ")
input_values=[]
input_values = input_number.split(",")
toc = time.time()
for i in input_values:
    fibonacci_sequence_of_linear(i)
tic = time.time()
time_taken=round((tic-toc)*1000, 1)
print ("{} milissegundos para calcular fibonacci da lista {} na versão monoprocessada linear.".format(time_taken,input_number))