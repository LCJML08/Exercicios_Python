'''Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. 
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''
sexo = ''
while sexo not in 'MF':
    sexo = str(input('Digite o sexo de uma pessoa: ')).strip().upper() [0]
    if sexo not in 'MF':
        print('{}Termo inválido{}'.format('\033[1;34m','\033[m'))
print('REGISTRADO')
