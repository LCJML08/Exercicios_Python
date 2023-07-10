'''Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer 
e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''
n = int(input('Digite um número: '))
print('=-='*10)
print('{}Selecione a conversão{}'.format('\033[1;34m','\033[m'))
print('=-='*10)
print('{}(1){} -> Hexadecimal'.format('\033[1;34m','\033[m'))
print('{}(2){} -> Octadecimal'.format('\033[1;34m','\033[m'))
print('{}(3){} -> Binário'.format('\033[1;34m','\033[m'))
opcao = int(input('Digite o número: '))
if opcao == 1:
    print(str(hex(n))[2:])
elif opcao == 2:
    print(str(oct(n))[2:])
elif opcao == 3:
    print(str(bin(n))[2:])
else:
    print('Esta opção não existe!')
    