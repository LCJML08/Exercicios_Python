'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, 
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''
c1 = c2 = c3 = 0
while True:
    s = opcao = '.'
    while s not in 'MF':
        s = str(input('Sexo: [M/F] ')).strip().upper()[0]
    i = 0
    while i <= 0:
        i = int(input('Idade: '))
    if i > 18:
        c1 += 1
    if s in 'M':
        c2 += 1
    if i < 20 and s in 'F':
        c3 += 1
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opcao in 'N':
            break
print(f'''Ao total são {c1} pessoas com mais de 18 anos de idade
      {c2} homens cadastrados e {c3} mulheres com menos de 20 anos.''')
