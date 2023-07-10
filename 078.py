'''Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''
n = []
for c in range(0,5):
    x = int(input(f'Digite um númeor inteiro: [{c+1}/5] '))
    n.append(x)
    if c == 0:
        maior = menor = x
    else:
        if maior < x:
            maior = x
            posicao_maior = c+1
        if menor > x:
            menor = x
            posicao_menor = c+1
print(f'Lista: {n}')
print(f'Maior: {maior}, na posição {posicao_maior}')
print(f'Menor: {menor}, na posição {posicao_menor}')
