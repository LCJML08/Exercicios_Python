from random import randint
from time import sleep
jogadores = 0
lista = {}
print('=== SORTEANDO OS VALORES ===')
sleep(2)
for c in range (0,4):
    jogadores = randint(0,6)
    print(f'Jogador {c+1} tirou: {jogadores}')
    lista[f'Jogador {c+1}'] = jogadores
    sleep(0.5)
print(lista)