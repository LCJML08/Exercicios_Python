#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
import random
from time import sleep
print('SUAS OPÇÕES: \n [ 0 ] PEDRA \n [ 1 ] PAPEL \n [ 2 ] TESOURA')
jogador = int(input('Qual a sua jogada? '))
l = ['PEDRA','PAPEL','TESOURA']
'''if x == 1:
    jogador = 'PEDRA' 
if x == 2:
    jogador = 'PAPEL' 
if x == 3:
    jogador = 'TESOURA' '''
computador = random.randint(0,2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-='*11)
print('Computador jogou {}'.format(l[computador]))
print('Jogador jogou {}'.format(l[jogador]))
print('-='*11)

if computador == 2 and jogador == 1 or computador == 0 and jogador == 2 or computador == 1 and jogador == 0:
    print('{}COMPUTADOR VENCEU !!!{}'.format('\033[1;34m','\033[m'))
elif computador == 2 == jogador or computador == 1 == jogador or computador == 0 == jogador:
    print('{}EMPATE !!!{}'.format('\033[1;34m','\033[m'))
elif computador == 1 and jogador == 2 or computador == 2 and jogador == 0 or computador == 0 and jogador == 1:
    print('{}JOGADOR VENCEU !!!{}'.format('\033[1;34m','\033[m'))
else:
    print('{}JOGADA INVÁLIDA{}'.format('\033[1;34m','\033[m'))
