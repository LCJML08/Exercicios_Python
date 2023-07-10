'''Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''
cor0 = '\033[m'
cor1 = '\033[1;34m'
c = 0
soma = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    c += 1
    soma += n
print(f'Você escreveu {cor1}{c}{cor0} números e a soma entre eles é {cor1}{soma}{cor0}')
