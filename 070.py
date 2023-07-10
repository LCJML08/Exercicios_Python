'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''
valor = total = caro = barato = itens = 0
while True:
    produto = continuar = '.'
    produto = str(input('Nome do produto: '))
    valor = float(input('Valor: R$'))
    total += valor
    itens += 1
    if valor > 1000:
        caro += 1
    if itens == 1 or valor < barato:
        barato = valor
        mais_barato = produto
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar as compras? [S/N] ')).upper().strip()
    if continuar in 'N':
        break
print(f'Você comprou um total de {itens} itens, e o valor total da compra foi de R${total:.2f}')
print(f'Na lista estão {caro} itens que custam mais de R$1.000,00 e o produto mais barato foi: {mais_barato} que custa R${barato:.2f}')
