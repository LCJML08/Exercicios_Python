'''Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''
n = int(input('Escolha um número para mostrar a tabuada dele: '))
for c in range(1,11):
    print('{} X {} = {}'.format(n,c,(n*c)))
