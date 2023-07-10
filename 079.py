'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''
lista = []
r = '.'
while r not in 'N':
    x = (int(input('Digite um número: ')))
    if x not in lista:
        lista.append(x)
    else:
        print('Esse número já foi adicionado!')
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
lista.sort()
print(f'Lista: {lista}')
