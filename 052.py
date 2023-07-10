#Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input('Digite um número: '))
d = 0
for c in range(1, n+1):
    if (n % c) == 0:
        print('{}{}{}'.format('\033[1;34m',c,'\033[m'), end = (' '))
        d += 1
    else:
        print(c, end = ' ')
print('O número {}, foi divisível {} vezes.'.format(n,d))
if d == 2:
    print('Por isso, ele é primo!')
else:
    print('Por isso ele não é primo!')
    