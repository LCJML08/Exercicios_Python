'''Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros termos dessa progressão.'''
p = int(input('Escreva o primeiro termo da PA: '))
r = int(input('Escreva agora a razão desta PA: '))
l = r*10
for c in range(p,l,r):
    print('{} '.format(c), end = "- ")
print('ACABOU')
