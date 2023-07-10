'''Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário 
se elas podem ou não formar um triângulo.'''
print("="*25)
print('\033[4;34mAnalisador de Triângulos\033[m')
print("="*25)
l1 = float(input('Digite a medida do 1° segmento: '))
l2 = float(input('Digite a medida do 2° segmento: '))
l3 = float(input('Digite a medida do 3° segmento: '))
print('Esses segmentos podem formar um triângulo!' if l1+l2>l3 and l2+l3>l1 and l3+l1>l2 else 'Esses segmentos não podem formar um triângulo!')
