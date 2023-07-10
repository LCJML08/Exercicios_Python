# o programa deve mostrar se o usuário acertou o número sorteado
import random
n = random.randrange(1,6)
o = int(input('Adivinhe qual número sorteado de 1 à 5 foi escolhido : '))
print("Acertou" if o == n else "Errou, o número escolhido foi {}".format(n))
