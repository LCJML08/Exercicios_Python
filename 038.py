#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os.
n1 = int(input('{}Digite um número:{} '.format('\033[1;32m','\033[m')))
n2 = int(input('{}Agora outro:{} '.format('\033[1;32m','\033[m')))
if n1 > n2:
    print('{}O primeiro número é maior!{}'.format('\033[1;35m','\033[m'))
elif n2 > n1:
    print('{}O segundo número é maior!{}'.format('\033[1;35m','\033[m'))
else:
    print('{}Os números são iguais!{}'.format('\033[1;35m','\033[m'))
    