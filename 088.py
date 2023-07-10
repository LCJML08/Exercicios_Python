from time import sleep
from random import randint
n = int (input('Digite quantos jogos quer sortear: '))
lista = []
jogos = []
for p in range (0,n):
    for c in range (0,6):
        while True:
            n1 = randint(1,60)
            if n1 not in lista:
                break
        lista.append(n1)
        lista.sort()
    jogos.append(lista[:])
    lista.clear()
for x, y in enumerate(jogos):
    print(f'Jogo {x+1}: {y}')
    sleep(0.5)
    