N1 = int(input("Limite inferior: "))
N2 = int(input("Limite superior: "))

produto = 1
contPrimo = 0

for c in range(N1 + 1, N2):
    cont = 0
    for i in range(1,c +1):
        if c % i == 0:
            cont += 1
    if cont <= 2:
        contPrimo += 1
        produto *= c
if contPrimo > 0:
    print(f'O produto dos primos entre {N1} e {N2} vale {produto}')
else:
    print(f'Não ha numeros primos entre {N1} e {N2}. o produto vale 0')