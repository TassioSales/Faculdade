# programa python para pesquisa linear usando loop while

#define list
lst = []

#take input list size
num = int(input("Insira o tamanho da lista :- "))

for n in range(num):
    #append element in list/array
    numbers = int(input("Insira a matriz of %d elemento :- " %n))
    lst.append(numbers)

#take input number to be find in list   
x = int(input("Digite o número para pesquisar na lista :- "))

i = 0
flag = False

while i < len(lst):
	if lst[i] == x:
		flag = True
		break

	i = i + 1

if flag == 1:
	print('{} foi encontrado no índice {}.'.format(x, i))
else:
	print('{} não foi encontrado.'.format(x))