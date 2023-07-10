#Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
b = 0
a = 0
for c in range(3,501,3):
    if (c % 2) != 0:
        b += 1
        a += c
print('A soma de todos os {} valores é de: {}'.format(b,a))
