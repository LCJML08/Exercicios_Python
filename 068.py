'''Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o 
jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
import random
c = 0
while True:
    jogador = int(input('Escolha um número: '))
    tipo = str(input('Voce quer par ou ímpar? [P/I]: ')).upper().strip()[0]
    computador = random.randint(1,10)
    soma = (jogador + computador)
    if soma % 2 == 0 and tipo == 'P' or soma % 2 != 0 and tipo == 'I':
        print(f'O computador escolheu {computador} e você escolheu {jogador}. \nA soma é {soma}', end = (' '))
        print('Deu Par' if soma % 2 == 0 else 'Deu Ímpar')
        print('Parabéns, você venceu!!! Vamos joga novamente!')
        c += 1
    else:
        print(f'O computador escolheu {computador} e você escolheu {jogador}. \nA soma é {soma}.', end = (' '))
        print('Deu Par' if soma % 2 == 0 else 'Deu Ímpar')
        print('Infelizmente você perdeu. Você ganhou {c} rodada(s)!')
        break
    