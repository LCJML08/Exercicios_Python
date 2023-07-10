'''Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''
valor = float(input('Digite quanto quer sacar: R$'))
while True:
    c = cedula = 0
    if valor >= 50:
        cedula = 50
    elif valor >= 20:
        cedula = 20
    elif valor >= 10:
        cedula = 10
    elif valor >= 1:
        cedula = 1
    while valor >= cedula:
        valor -= cedula
        c += 1
    print(f'Serão emitidas {c} cédulas de R${cedula:.2f}')
    if valor == 0:
        break
print('Tenha um bom dia!')
