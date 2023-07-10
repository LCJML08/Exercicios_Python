'''Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''
lista = []
e = 0
for c in range (0,5):
    n = int(input('Digite um número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print(f'{n} foi adicionado ao final da lista!')
    else:
        e = 0
        while n > lista[e]:
            e += 1
        lista.insert(e,n)
        print(f'O número foi inserido na posição {e}')
print(f'Os valores digitados na lista foram: {lista}')
