'''Exercício Python 63: Escreva um programa que leia um 
número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:'''
n = int(input('Digite quantos termos você quer ver: '))
t3 = 0
t2 = 1
t1 = 0
print('{} -> {} -> '.format(t1,t2), end = (''))
while n != 0:
    t3 = t1 + t2
    print(t3, end = ' -> ')
    t1 = t2
    t2 = t3
    n -= 1
print('FIM')
