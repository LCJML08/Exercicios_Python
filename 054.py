'''Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1,8):
    ano = int(input('Digite o ano em que a {}° pessoa nasceu: '.format(c)))
    if atual - ano >= 18:
        maior += 1
    else:
        menor += 1
print('Ao todo temos {} pessoas que são maiores de idade e {} menosres de idade'.format(maior,menor))
