'''Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''
p1 = int(input('Escreva o primeiro termo: '))
r = int(input('Agora escreva a razão: '))
c = p1
limite = p1 + (r*10)
while c != limite:
    print('{}'.format(c), end = " -> ")
    c += r
print('FIM')
    