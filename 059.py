'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''
opcao = 0
while opcao != 5:    
    n1 = int(input('Digite o 1° número: '))
    n2 = int(input('Digite o 2° número: '))
    print('{:-^30}'.format(' SELECIONE UMA OPÇÃO '))
    print('{}[1]{} - Somar'.format('\033[1;34m','\033[m'))
    print('{}[2]{} - Multiplicar'.format('\033[1;34m','\033[m'))
    print('{}[3]{} - Maior'.format('\033[1;34m','\033[m'))
    print('{}[4]{} - Novos Números'.format('\033[1;34m','\033[m'))
    print('{}[5]{} - Sair do Programa'.format('\033[1;34m','\033[m'))
    opcao = int(input('Sua opção: '))
    if opcao == 1:
        print(n1+n2)
    elif opcao == 2:
        print(n1*n2)
    elif opcao == 3:
        if n1 > n2:
            print(n1)
        else:
            print(n2)
    elif opcao != 4 and opcao != 5:
        print('Esta opção é inválida')
print('FIM')
