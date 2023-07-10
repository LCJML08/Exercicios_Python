'''Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário 
se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.'''
p1 = int(input('Escreva o primeiro termo: '))
r = int(input('Agora escreva a razão: '))
c = p1
opcao = 10
total = 0
limite = 0
while opcao != 0:
    total += opcao
    limite = p1 + (r*total)
    while c != limite:
        print('{}'.format(c), end = " -> ")
        c += r
    opcao = int(input('Quantos termos a mais quer mostrar? '))
print('FIM')
    