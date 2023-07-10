'''Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''
maior = 0
menor = 0
for c in range(1,6):
    peso = float(input('Digite o peso da {}° pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    elif maior < peso:
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior peso digitado foi {:.2f}KG e o menor peso foi {:.2f}KG'.format(maior,menor))
