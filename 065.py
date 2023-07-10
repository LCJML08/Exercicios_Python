'''Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, 
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
sn = ''
menor = media = soma = maior = c = 0
while sn != 'N':
    n = int(input('Digite um número: '))
    c += 1
    soma += n
    if c == 1:
        menor = n
        maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    sn = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
media = soma / c
print('''Você digitou {} números
A média entre eles é {:.2f}
O menor valor digitado é {} e o maior valor digitado é {}'''.format(c,media,menor,maior))
