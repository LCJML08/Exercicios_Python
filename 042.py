'''Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

 EQUILÁTERO: todos os lados iguais

 ISÓSCELES: dois lados iguais, um diferente

 ESCALENO: todos os lados diferentes'''
print("="*25)
print('\033[4;34mAnalisador de Triângulos\033[m')
print("="*25)
l1 = float(input('Digite a medida do 1° segmento: '))
l2 = float(input('Digite a medida do 2° segmento: '))
l3 = float(input('Digite a medida do 3° segmento: '))
i = 0
if l1+l2>l3 and l2+l3>l1 and l3+l1>l2:
    print('Esses segmentos podem formar um triângulo!')
    if l1 == l2 == l3:
        print('Do tipo: EQUILÁTERO')
    elif l1 != l2 != l3 != l1:
        print('Do tipo: ESCALENO')
    else: 
        print('Do tipo: ISÓSCELES')
else:
    print('Esses segmentos não podem formar um triângulo!')
