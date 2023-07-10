'''Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços'''
frase = str(input('Digite um frase: ')).strip().upper().split()
frase = ''.join(frase)
letras = len(frase)
palavra = str('')
for c in range(letras-1,-1,-1):
    palavra += frase[c]
if palavra == frase:
    print('O inverso de {} é {} \n Essa frase é um palíndromo'.format(frase,palavra))
else:
    print('O inverso de {} é {} \n Essa frase não é um palíndromo'.format(frase,palavra))
