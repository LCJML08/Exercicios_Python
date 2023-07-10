'''Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo.'''
c = 1
while True:
    t = int(input('Você quer ver a tabuada de qual valor? '))
    if t <= 0:
        break
    while c != 11:
        print(f'[{t}] X [{c}] = {t*c}')
        c += 1
    c = 1
print('PROGRAMA FINALIZADO')
