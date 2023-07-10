'''Exercício Python 50: Desenvolva um programa que leia 
seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.'''
a = 0
b = 0
for c in range(0,6):
    n = int(input('Digite o {}° número: '.format(c+1)))
    if (n % 2) == 0:
        b += 1
        a += n
print('A soma de todos os números pares ({}) que foram digitados é: {}'.format(b,a))
