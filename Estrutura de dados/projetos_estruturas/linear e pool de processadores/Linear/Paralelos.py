from multiprocessing import Pool
import time


def fibonacci_sequence_of_paralelos(num):
    first_number = 0
    second_number = 1

    num = int(num)
    if num == 0:
        print("Fibonacci {} é {}".format(num, num))
    elif num == 1:
        print("Fibonacci {} é {}".format(num, num))
    else:
        for i in range(2, num):
            new_number = first_number + second_number
            first_number = second_number
            second_number = new_number
    print("Fibonacci {} é {}".format(num, second_number))


if __name__ == '__main__':
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
