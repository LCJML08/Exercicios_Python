'''Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
import random
n = random.randrange(1,6)
o = c = 0
while o != n:
    o = int(input('Adivinhe qual número sorteado de 1 à 5 foi escolhido : '))
    if o != n:
        print("Errou, o número escolhido foi {}".format(n))
    c += 1
print("Acertou, você precisou de {} tentativas para acertar!".format(c))
