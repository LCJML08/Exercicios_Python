'''Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''
nome = ''
idade = 0
mais_velho = 0
sexo = ''
soma = 0
media = 0
contador = 0
posicao = ''
for c in range(1,5):
    print('{:-^20}'.format(f' Pessoa {c} '))
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('M/F: ')).strip().upper()
    soma += idade
    if sexo == 'M' and idade > mais_velho:
            mais_velho = idade
            posicao = nome
    elif sexo == 'F' and idade < 20:
        contador += 1
media = soma // 4
print('A média das idades é: {}'.format(media))
print('O homem mais velho é: {} com {} anos'.format(posicao,mais_velho))
print('Existem {} mulheres com menos de 20 anos'.format(contador))
