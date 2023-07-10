'''Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''
palavras = ('PROGRAMADOR','COMPUTADOR','TECLADO','MONITOR','PYTHON','TECNOLOGIA','CURSO')
vogais = 'aeiou'
for c in palavras:
    print(f'\nA palavra {c} tem as vogais: ', end = (' '))
    if 'A' in c:
        print('a ', end = (' '))
    if 'E' in c:
        print('e ', end = (' '))
    if 'I' in c:
        print('i ', end = (' '))
    if 'O' in c:
        print('o ', end = (' '))
    if 'U' in c:
        print('u ', end = (' '))
        