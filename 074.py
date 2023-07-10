'''Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''
from random import randint
c = menor = maior = 0
numeros = (randint(1,9),randint(1,9),randint(1,9),randint(1,9),randint(1,9))
print(f'Os numeros sorteados foram: {numeros}')
'''
for n in numeros:
    if c == 0:
        menor = n
        maior = n
    elif n < menor:
        menor = n                                           #OUTRA FORMA DE FAZER
    elif n > maior:
        maior = n
    c += 1
print(f'O maior número é : {maior}')
print(f'O menor número é: {menor}')
'''
print(f'O maior número é : {max(numeros)}')
print(f'O menor número é: {min(numeros)}')
