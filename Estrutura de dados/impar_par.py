#Declarando variaveis quem pedem para o usuario o limite superior e inferior
num1 =  1
num2 =  20

#Declarando variaveis para somatorio
somaimpa = 0
somapar = 0

print(f'Os numeros impares encontrado no intervalo de {num1} a {num2} e ', end =' ')
#Repetição for que vai do limite inferior ate o limite superior
for c  in range(num1, num2 + 1):
    #condição que imprime os numeros impares e faz o somatorio
    if c % 2 == 1:
        print(f'{c}', end = ' ')
        somaimpa += c

print(f'\nOs numeros pares encontrado no intervalo de {num1} a {num2} e ', end =' ')
#Repetição for que vai do limite inferior ate o limite superior
for i  in range(num1, num2 + 1):
    #condição que imprime os numeros impares e faz o somatorio
    if i % 2 == 0:
        print(f'{i}', end = ' ')
        somapar += i

print(f'\nA soma  dos numeros impares encontrado e {somaimpa}')
print(f'A soma  dos numeros pares encontrado e {somapar}')             
