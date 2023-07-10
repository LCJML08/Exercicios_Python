'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.'''
i = c = nove = 0
pares = ()
tupla = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Mais um: ')), int(input('O último agora: ')))
print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O valor 3 foi digitado primeiramente na {tupla.index(3) + 1}ª solicitação')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os números pares digitados foram:', end = (' '))
for c in tupla:
    if c % 2 == 0:
        print(c, end = (' '))
        i += 1
if i == 0:
    print('(Não foram digitados números pares)')
    