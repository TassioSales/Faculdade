import os
from time import sleep

# 20/03/2021
# ALUNOS: TASSIO SALES, PEDRO MAGALHAES, ROBSON LUIS


pessoas = []


def adicionar(pessoa):
    qtd = int(input('Quantas pessoas deseja adicionar: '))
    for c in range(0, qtd):
        os.system('cls')
        nome = str(input('NOME : ')).strip().upper()
        idade = int(input('IDADE: '))
        sexo = str(input('SEXO [M/F]: ')).strip().upper()
        while sexo not in "MF":
            sexo = str(input('SEXO [M/F]: ')).strip().upper()
        pessoa.append([nome, idade, sexo])


def verLista(visualizar):
    contNome = 0
    contIdade = 1
    contSexo = 2
    print(f'{"ID":<10}{"NOME":<15}{"IDADE":^10}{"SEXO":>10}')
    for c in range(0, len(visualizar)):
        print('-' * 50)
        print(f'{c}{visualizar[c][contNome]:>12}{visualizar[c][contIdade]:>16} '
              f'{visualizar[c][contSexo]:>13}')
        c += 1
    while True:
        des = str(input('Digite S para retorna ao menu ?[S]')).strip().upper()[0]
        if des == 'S':
            print('Retornando ao MENU')
            break
        else:
            print('OPCÃO INVALIDA')


def excluir(exclusao):
    for item in exclusao:
        print(f'ID:{exclusao.index(item)} NOME: {item[0]} IDADE: {item[1]} SEXO: {item[2]}')
    while True:
        opcao = int(input("ID que deseja excluir: "))
        del (exclusao[opcao])
        print('ID nao encontrado')
        print("PESSOA EXCLUIDA")
        esc = str(input('Deseja excluir mais alguem ?[S/N]')).strip().upper()[0]
        if esc == 'S':
            for item in exclusao:
                print(f'ID:{exclusao.index(item)} NOME: {item[0]} IDADE: {item[1]} SEXO: {item[2]}')
            continue
        else:
            print('RETORNANDO AO MENU')
            break


while True:
    os.system('cls')
    print(F'''{'MENU':.^30}
    [ 1 ] ADICIONAR NOME
    [ 2 ] VER LISTA
    [ 3 ] EXCLUIR
    [ 4 ] FINALIZAR''')
    opc = int(input('Digite a opção desejada:'))

    if opc == 1:
        adicionar(pessoas)
        sleep(2)
        os.system('cls')
    elif opc == 2:
        verLista(pessoas)
        sleep(2)
        os.system('cls')
    elif opc == 3:
        excluir(pessoas)
        sleep(2)
        os.system('cls')
    elif opc == 4:
        print('OBRIGADO POR USAR O PROGRAMA')
        break
    else:
        print("opção invalida")
        sleep(2)
